# ASCII Art (TT PROJECT 2) ✅

A tiny Python script that reconstructs and prints a large ASCII art image from a run-length encoded (RLE) representation.

## Quick start 🔧

- Run:

```bash
python -u "asciiart.py"
```

- The script prints the ASCII art directly to stdout.

## How it works 💡

- The RLE data is stored in `RLE_TEXT` (a triple-quoted block) and parsed at runtime into a `rle` list of `(count, char)` tuples.
- `reconstruct_ascii_from_rle()` iterates rows and groups to build and print each line.

## Editing the artwork ✏️

- You can edit `RLE_TEXT` directly, or replace it with a valid Python `rle = [...]` literal (ensure commas are present between rows).
- If you want, I can restore the original literal form (fix missing commas) so the file contains a Python list instead of a parsed string.

## Troubleshooting ⚠️

- If the program prints nothing or errors on startup, run it with `-u` to avoid buffering: `python -u "asciiart.py"`.
- If you see a `SyntaxError`, open `asciiart.py` and ensure `RLE_TEXT` is intact.

## Contributing 🤝

- Feel free to open edits or request improvements (unit tests, recovery of the original literal, or more documentation).

---

*Generated/updated by GitHub Copilot.*