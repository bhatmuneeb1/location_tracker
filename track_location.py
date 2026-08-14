#!/usr/bin/env python3
"""Offline IP geolocation CLI using a local MaxMind database.

No queried IP addresses are sent to a remote service. Users provide their own
GeoLite2/GeoIP2 City database file.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
from pathlib import Path
from typing import Any, Sequence


def parse_ip(value: str) -> str:
    """Validate and normalize an IPv4 or IPv6 address."""
    return str(ipaddress.ip_address(value.strip()))


def lookup_ip(database: Path, ip: str) -> dict[str, Any]:
    try:
        import geoip2.database
    except ImportError as exc:
        raise RuntimeError("geoip2 is not installed; run: python -m pip install -e .") from exc

    if not database.is_file():
        raise FileNotFoundError(database)

    with geoip2.database.Reader(str(database)) as reader:
        response = reader.city(ip)

    return {
        "ip": ip,
        "country": response.country.name,
        "country_iso": response.country.iso_code,
        "subdivision": response.subdivisions.most_specific.name,
        "city": response.city.name,
        "postal_code": response.postal.code,
        "latitude": response.location.latitude,
        "longitude": response.location.longitude,
        "accuracy_radius_km": response.location.accuracy_radius,
        "time_zone": response.location.time_zone,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Look up an IP address using a local MaxMind GeoLite2/GeoIP2 City database"
    )
    parser.add_argument("ip", help="IPv4 or IPv6 address to look up")
    parser.add_argument("--database", "-d", required=True, type=Path, help="path to a local .mmdb City database")
    parser.add_argument("--json", action="store_true", dest="as_json", help="print machine-readable JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        ip = parse_ip(args.ip)
        result = lookup_ip(args.database.expanduser(), ip)
    except (ValueError, FileNotFoundError, RuntimeError) as exc:
        print(f"error: {exc}")
        return 2
    except Exception as exc:  # geoip2 address-not-found and database errors
        print(f"lookup failed: {exc}")
        return 1

    if args.as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"IP: {result['ip']}")
        print(f"Country: {result['country'] or 'unknown'} ({result['country_iso'] or '-'})")
        print(f"Subdivision: {result['subdivision'] or 'unknown'}")
        print(f"City: {result['city'] or 'unknown'}")
        print(f"Postal code: {result['postal_code'] or 'unknown'}")
        print(f"Coordinates: {result['latitude']}, {result['longitude']}")
        print(f"Accuracy radius: {result['accuracy_radius_km']} km")
        print(f"Time zone: {result['time_zone'] or 'unknown'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
