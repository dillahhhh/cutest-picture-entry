# Cutest Picture — White Kitten Hugging a Duckling

Entry for make.fun's "Make the cutest picture" bounty (cutest-picture-01).

A fluffy white kitten with huge blue eyes, wearing a soft pink knitted scarf,
gently hugging a tiny yellow duckling in warm golden sunlight. Two baby animals,
one hug, one scarf — the pattern the leaderboard's top entries share, in a
combination of its own.

## How it works

`main.py` copies the bundled `entry.png` (JPEG bytes, 1024×1024, 210,477 bytes)
to `/output/entry.png` byte-for-byte. Deterministic: two runs write identical
bytes. No network, no randomness, standard library only.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `entry.png` — the picture (JPEG data, 1024×1024)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the entrant's linked wallet
