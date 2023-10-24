import secrets
import time
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, Generic, List, Optional, TypeVar, cast
from urllib.parse import urlencode

import httpx
import jwt
from jwt.algorithms import RSAAlgorithm

from kt2.errors import OAuthError

algorithm = RSAAlgorithm(RSAAlgorithm.SHA384)

# Move into settings helper?
with open('./.keys/private.pem') as keyfile:
    private_key = algorithm.prepare_key(keyfile.read())


class GetAccessTokenError(OAuthError):
    pass


class RefreshTokenError(OAuthError):
    pass


class RevokeTokenError(OAuthError):
    pass


class OAuth2Token(Dict[str, Any]):
    def __init__(self, token_dict: Dict[str, Any]):
        if "expires_at" in token_dict:
            token_dict["expires_at"] = int(token_dict["expires_at"])
        elif "expires_in" in token_dict:
            token_dict["expires_at"] = int(time.time()) + int(token_dict["expires_in"])
        super().__init__(token_dict)

    @property
    def bearer_token(self) -> str:
        access_token = self.get("access_token", None)
        if not access_token:
            return ""

        print("token headers", jwt.get_unverified_header(access_token))
        print(
            "unverified token",
            jwt.decode(access_token, options={"verify_signature": False}),
        )
        return f'Bearer {access_token}'

    def is_expired(self):
        if "expires_at" not in self:
            return True
        return time.time() > self["expires_at"]


T = TypeVar("T")


class SmartFHIROAuth2(Generic[T]):
    name: str
    client_id: str
    authorize_endpoint: str
    access_token_endpoint: str
    introspection_token_endpoint: Optional[str]
    base_scopes: List[str] = []
    request_headers: Dict[str, str]
    enable_logger: bool = False

    def __init__(
        self,
        client_id: str,
        authorize_endpoint: str,
        access_token_endpoint: str,
        fhir_url: str,
        introspection_token_endpoint: Optional[str] = None,
        name: str = "smart-on-fhir",
    ):
        self.client_id = client_id
        self.authorize_endpoint = authorize_endpoint
        self.access_token_endpoint = access_token_endpoint
        self.fhir_url = fhir_url
        self.introspection_token_endpoint = introspection_token_endpoint
        self.name = name

        self.token: OAuth2Token = None

        self.request_headers = {
            "Accept": "application/json",
        }

    @property
    def token(self) -> OAuth2Token:
        return self._token

    @token.setter
    def token(self, value) -> None:
        self._token = value

    async def get_authorization_url(
        self,
        redirect_uri: str,
        state: Optional[str] = None,
        scope: Optional[List[str]] = None,
        extras_params: Optional[T] = None,
    ) -> str:
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": redirect_uri,
            "code_challenge": secrets.token_urlsafe(),
            "code_challenge_method": "S256",
        }

        if state is not None:
            params["state"] = state

        # Provide compatibility with current scope from the endpoint
        _scope = scope or self.base_scopes
        if _scope is not None:
            params["scope"] = " ".join(_scope)

        if extras_params is not None:
            params = {**params, **extras_params}  # type: ignore

        return f"{self.authorize_endpoint}?{urlencode(params)}"

    async def get_access_token(self):
        async with httpx.AsyncClient() as client:
            payload = {
                "iss": self.client_id,
                "sub": self.client_id,
                "exp": datetime.now() + timedelta(minutes=5),
                "aud": self.access_token_endpoint,
                "jti": str(uuid.uuid4()),
            }

            token = jwt.encode(
                payload,
                private_key,
                algorithm="RS512",
                headers={"alg": "RS512", "kid": "edge-jouwomgeving", "typ": "JWT"},
            )

            data = {
                'client_assertion': token,
                'client_assertion_type': (
                    'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
                ),
                'grant_type': "client_credentials",
                "aud": self.fhir_url,
                'scope': "",
            }

            token_headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                **self.request_headers,
            }

            self.logger.info("== AcccesToken flow ==")
            self.logger.info(f"data: {data}")
            self.logger.info(f"url:  {self.access_token_endpoint}")
            self.logger.info(f"headers: {token_headers}")

            response = await client.post(
                self.access_token_endpoint,
                data=data,
                headers=token_headers,
            )

            if not response.is_success:
                # return empty token
                empty_token = OAuth2Token({})
                self.token = empty_token
                return empty_token

            data = cast(Dict[str, Any], response.json())

            if response.status_code == 400:
                raise GetAccessTokenError(data)

            # Set token on client and return for further processing
            token = OAuth2Token(data)

            # Store on client
            self.token = token

            return token

    async def introspect_token(self, access_token: str):
        ...


OAuth2 = SmartFHIROAuth2[Dict[str, Any]]
