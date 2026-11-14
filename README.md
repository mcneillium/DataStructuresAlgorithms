# Data Structures & Algorithms in Python

[![tests](https://github.com/mcneillium/DataStructuresAlgorithms/actions/workflows/tests.yml/badge.svg)](https://github.com/mcneillium/DataStructuresAlgorithms/actions/workflows/tests.yml)

Three core data structures written from scratch in plain Python, with a
Tkinter GUI for trying them out and pytest tests for each.

Case study: [paulmartinmcneill.com/projects/data-structures-python](https://paulmartinmcneill.com/projects/data-structures-python/)

## What's inside

| Folder | Structure | Operations |
| --- | --- | --- |
| `trees/` | Binary search tree | insert, in-order traversal (returns keys sorted) |
| `graphs/` | Directed graph (adjacency list) | add edge, breadth-first search |
| `hash_tables/` | Hash table with separate chaining | set, get, delete, `in`; colliding keys are kept |
| `main_gui.py` | Tkinter GUI | one tab per structure, with input checks and explanations |
| `tests/` | pytest | 7 tests covering each structure |

## Run it

Python 3.10 or later. The code uses only the standard library; Tkinter ships
with most Python installs (on Linux: `sudo apt install python3-tk`).

```bash
git clone https://github.com/mcneillium/DataStructuresAlgorithms.git
cd DataStructuresAlgorithms
python main_gui.py        # opens the GUI
pip install pytest
python -m pytest -q       # runs the tests
```

## Changes since the first version (November 2026)

- **Breadth-first search** no longer crashes when an edge points to a
  higher-numbered vertex than any source vertex (it used a list sized by the
  largest source). It now uses a set and a deque, and works with any vertex
  type.
- **Hash table** now keeps keys whose hashes collide (for example `"ab"` and
  `"ba"`); before, the second silently overwrote the first. Missing keys raise
  `KeyError`.
- Added tests, continuous integration, and a `.gitignore`; removed committed
  `__pycache__` files.

## Licence

MIT, see [LICENSE](LICENSE).
