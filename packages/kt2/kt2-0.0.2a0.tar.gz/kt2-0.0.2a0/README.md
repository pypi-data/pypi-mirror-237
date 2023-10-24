## Features

Some of it’s stand out features are:

- Koppeltaal Api client

## Development

## Usage

### Configuration

Create a `koppeltaal.toml` file with the neccessary configuration:

```toml

client_name = "name-of-customer-or-client"
fhir_url = "https://foo.koppeltaal.nl/api/v1/healthcareinc/fhir/r4/"
oauth_token_url = "https://foo.koppeltaal.nl/api/v1/healthcareinc/oauth2/token"
oauth_authorize_url = "https://foo.koppeltaal.nl/api/v1/healthcareinc/oauth2/authorize"
oauth_introspection_token_url = "https://foo.koppeltaal.nl/api/v1/healthcareinc/oauth2/token/introspection"
smart_config_url = "https://foo.koppeltaal.nl/api/v1/healthcareinc/fhir/r4/.well-known/smart-configuration"
domain = "https://foo.koppeltaal.nl"
client_id = "uuid-client-id"


```

### Commandline interface

`kt2 help`

```
Usage: kt2 [OPTIONS] COMMAND [ARGS]...

  Koppeltaal command line tool

Options:
  --debug        enable debug logs ( default: False )
  --config TEXT  select config file
  --help         Show this message and exit.

Commands:
  activitydefinition   get single activitydefinition resource by id from
                       koppeltaal api
  activitydefinitions  get all activitydefinition resources from koppeltaal
                       api
  endpoint             get single endpoint resource by id from koppeltaal api
  endpoints            get all endpoint resources from koppeltaal api
  info                 show Koppeltaal api info
  patient              get single patient resource by id from koppeltaal api
  patients             get all patient resources from koppeltaal api
  practitioner         get single practitioner resource by id from koppeltaal
                       api
  practitioners        get all practitioner resources from koppeltaal api
  task                 get single task resource by id from koppeltaal api
  tasks                get all task resources from koppeltaal api
  version              show Koppeltaal cli version
```

### Python Shell

```shell
make shell
```

## Documentation

## Roadmap

-

## Is it any good?

[Yes.](http://news.ycombinator.com/item?id=3067434)

## License

The MIT License
