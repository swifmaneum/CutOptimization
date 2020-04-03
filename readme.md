# Cut Optimization
## Installation

The MiniZinc Python interface requires, see the [docs](https://minizinc-python.readthedocs.io/en/latest/getting_started.html#getting-started):
- [MiniZinc](https://www.minizinc.org/) 2.3.2 (or higher)
- Python 3.6 (or higher)

Then run
```
pip install requirements.txt
```

## Running
Adjust and run the `GeostModelRunner.py`

```python
# Panel describes the base area to place the 
# parts on by its x and y dimension.
panel = Part(2000, 2000)

# Parts are the parts to place on the panel.
# Parts can be symmetric.
# Order of x and y dimensions is arbitrary.
parts = [Part(1800, 100), Part(1800, 100)]
```