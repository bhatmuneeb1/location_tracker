# Contributing

Contributions are welcome, especially improvements to validation, output formats, testing, privacy, documentation, and support for local GeoIP database workflows.

## Development

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
ip-location --help
```

## Guidelines

- keep lookups local by default
- do not add telemetry or silent network requests
- add tests for behavior changes
- avoid committing MaxMind database files
- document user-visible changes clearly

Please keep pull requests focused and explain the practical benefit of the change.
