# Offline IP Geolocation

A small privacy-conscious command-line tool for looking up IPv4 and IPv6 addresses against a **local** MaxMind GeoLite2/GeoIP2 City database.

Unlike hosted IP lookup services, this tool does not send queried IP addresses to a third-party API. The database stays on your machine and lookups happen locally.

## Use cases

- incident-response enrichment
- log analysis
- privacy-conscious IP geolocation
- network troubleshooting
- learning how GeoIP databases work

IP geolocation is approximate. It should not be used to claim a person's exact physical location.

## Install

```bash
python -m pip install -e .
```

Download a legitimate GeoLite2 City or GeoIP2 City `.mmdb` database from MaxMind under the terms that apply to your account/database, then run:

```bash
ip-location 8.8.8.8 --database ~/GeoLite2-City.mmdb
```

JSON output:

```bash
ip-location 8.8.8.8 --database ~/GeoLite2-City.mmdb --json
```

IPv6 is supported too:

```bash
ip-location 2001:4860:4860::8888 --database ~/GeoLite2-City.mmdb
```

## Privacy design

- no hosted lookup API
- no telemetry
- no automatic network requests
- no database bundled in this repository
- IP input is validated with Python's standard `ipaddress` module

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Responsible use

GeoIP data normally resolves to an approximate network location, not a precise device or person. Do not present the output as GPS-level tracking or use it to harass, stalk, or target individuals.

## Contributing

Contributions that improve parsing, output formats, testing, documentation, or privacy are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. MaxMind databases are **not** included and are governed by their own license terms.
