"""Cutest picture entry: copy the bundled image to /output/entry.png.

Deterministic: reads the exact bytes of entry.png beside this file and
writes them unchanged. No network, no randomness, no timestamps.
Standard library only (Python 3.13).

Note on the file: entry.png holds JPEG bytes (1024x1024, 248,195 bytes,
sha256 f64a18ebfa931cc4b81b14bcb8cffa81eab394310f0eae5024fefdf137de6fe0). The
competition tells PNG and JPEG apart by their first bytes and the name
stays entry.png either way. JPEG is used because the same picture as PNG
is ~1.3 MB, over the 1 MiB cap — and a smaller file wins an exact
win-rate tie, so the compact encoding is strictly better here.

The picture: a tiny tabby kitten hugging a tiny pink piglet, both with
huge sparkling blue eyes looking at the camera, pink bows and daisy
flower crowns, on a pink background with hearts and bubbles.
"""

import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
dst = os.path.join(DST_DIR, "entry.png")
shutil.copyfile(SRC, dst)

# Self-check: the copy must be byte-identical to the source.
def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

assert _sha256(SRC) == _sha256(dst), "output differs from bundled image"

# Gate validation: the written file must satisfy the competition limits
# (whole JPEG, at most 1 MiB, at most 1024x1024). Dimensions are read from
# the JPEG SOF0/SOF2 marker with the standard library only.
def _jpeg_dimensions(path):
    with open(path, "rb") as f:
        data = f.read()
    assert data[:2] == b"\xff\xd8", "not a JPEG file"
    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            i += 1
            continue
        # Skip 0xFF fill bytes and the 0xFF00 escape (a literal 0xFF byte
        # inside entropy data), which carry no marker.
        if data[i + 1] in (0xFF, 0x00):
            i += 2
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            h = int.from_bytes(data[i + 5:i + 7], "big")
            w = int.from_bytes(data[i + 7:i + 9], "big")
            return w, h
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        length = int.from_bytes(data[i + 2:i + 4], "big")
        i += 2 + length
    raise ValueError("no JPEG SOF marker found")

w, h = _jpeg_dimensions(dst)
assert w <= 1024 and h <= 1024, f"image too large: {w}x{h}"
assert os.path.getsize(dst) <= 1048576, "image over 1 MiB"

print(f"wrote {dst}: {w}x{h} JPEG, {os.path.getsize(dst)} bytes, "
      f"sha256 {_sha256(dst)[:16]}...")
