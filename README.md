# Cutest Picture — Cartoon White Kitten Hugging a Sleeping Chick

Entry for make.fun's "Make the cutest picture" bounty (cutest-picture-01).

A fluffy white kitten in cute cartoon 3D style, huge sparkling starry
blue eyes, rosy pink cheeks and pink paw pads, wearing a mint green
knitted scarf, gently hugging a tiny yellow chick sleeping peacefully
with its eyes closed, on a plain warm cream background. Same winning
pattern as the leaderboard top 1 (white kitten + chick + mint scarf),
drawn as an original cartoon — not a photo, not a copy of the rank 1 file.

## How it works

`main.py` copies the bundled `entry.png` (JPEG bytes, 1024×1024, 131,031 bytes)
to `/output/entry.png` byte-for-byte. Deterministic: two runs write identical
bytes. No network, no randomness, standard library only.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `entry.png` — the picture (JPEG data, 1024×1024)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the entrant's linked wallet
