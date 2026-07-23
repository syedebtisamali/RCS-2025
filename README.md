# RCS-2025 Cube Simulator

A small Rubik's Cube simulator implemented in Python, with a matching C version in `cube.c`.

## Features

- In-memory cube model with six faces
- Face rotations for `U`, `D`, `R`, `L`, `F`, and `B`
- Text-based cube display in the terminal
- Simple demo entry point in `main.py`

## Project Layout

- `main.py` - Python demo entry point
- `cube.py` - Python cube model, display, and move logic
- `cube.c` - C version of the same cube logic

## Requirements

- Python 3.10 or newer
- No third-party Python packages are required

## Quick Start

Run the Python demo:

```bash
python3 main.py
```

Or execute the standalone cube module directly:

```bash
python3 cube.py
```

## C Version

The repository also includes a C implementation for reference. You can build it with a standard C compiler, for example:

```bash
cc cube.c -o cube
./cube
```

## Notes

- The project currently uses a simple list-based cube representation.
- The move functions mutate the cube in place.
- `main.py` demonstrates a short sample sequence of moves and prints the cube before and after.
