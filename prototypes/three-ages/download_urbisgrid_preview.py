#!/usr/bin/env python3
"""Download a small, source-linked urbisgrid 2022 orthophoto preview for the pilot.

The 2022 layer is served by urban.brussels's urbisgrid WMS. Reuse terms: the
official Ortho info page states CC0 for the urbisgrid ortho layers, while the
INSPIRE distribution record requires CC-BY attribution; both are satisfied by
this pilot's source linking. WMS 1.1.1 + SRS EPSG:4326 is required (1.3.0 +
CRS:84 returns blank tiles from this server).
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "data" / "urbisgrid-2022-grand-place.png"
WMS_URL = "https://geoservices-urbis.irisnet.be/geoserver/urbisgrid/wms"
LAYER = "urbisgrid:Ortho2022Ns"
BBOX = "4.348,50.845,4.357,50.849"
WMS_VERSION = "1.1.1"
SRS = "EPSG:4326"
PNG_HEADER = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "871d995a3753d2d03c811a5c59c1686b97b6ced87ae718a49481a743a2340ea5"
MAX_RESPONSE_BYTES = 10 * 1024 * 1024


def read_response(response) -> bytes:
    body = response.read(MAX_RESPONSE_BYTES + 1)
    if len(body) > MAX_RESPONSE_BYTES:
        raise RuntimeError(f"WMS response exceeds {MAX_RESPONSE_BYTES:,} bytes")
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    params = {
        "service": "WMS",
        "version": WMS_VERSION,
        "request": "GetMap",
        "layers": LAYER,
        "styles": "",
        "format": "image/png",
        "transparent": "true",
        "width": 640,
        "height": 480,
        "srs": SRS,
        "bbox": BBOX,
    }
    url = f"{WMS_URL}?{urlencode(params)}"
    with urlopen(Request(url, headers={"User-Agent": "final-work-three-ages/1.0"}), timeout=60) as response:
        body = read_response(response)
    if not body.startswith(PNG_HEADER):
        raise RuntimeError(f"WMS returned a non-PNG response: {body[:120]!r}")
    digest = hashlib.sha256(body).hexdigest()
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"2022 WMS preview checksum changed: {digest}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(body)
    args.output.chmod(0o644)
    try:
        display_output = args.output.relative_to(ROOT)
    except ValueError:
        display_output = args.output
    print(f"wrote {display_output}")
    print(f"source layer: {LAYER}; bbox: {BBOX}; wms {WMS_VERSION} {SRS}")


if __name__ == "__main__":
    main()