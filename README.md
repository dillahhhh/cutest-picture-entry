# Cutest Picture — Tabby Kitten Hugging a Tiny Piglet

Entry for make.fun's "Make the cutest picture" bounty (cutest-picture-01).

A tiny tabby kitten hugging a tiny pink piglet, both with huge sparkling
blue eyes looking straight at the camera, pink bows and daisy flower
crowns, on a soft pink background with hearts and bubbles. Two baby
animals, one hug, big eyes — the pattern the leaderboard's top entries
share (kitten hugging a chick/duckling), in a combination of its own:
kitten + piglet, eyes open to the camera.

## How it works

`main.py` copies the bundled `entry.png` (JPEG bytes, 1024×1024, 248,195 bytes)
to `/output/entry.png` byte-for-byte. Deterministic: two runs write identical
bytes. No network, no randomness, standard library only.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `entry.png` — the picture (JPEG data, 1024×1024)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the entrant's linked wallet
