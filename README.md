# typah
An insanely simple application to auto type. Supports multi line, repeat, random key delays, set key delays. Uses OOP


# Usage
```
pip install git+https://github.com/logixhot/typah.git
```

```python
from typah import typah

Typer = typah.Typer()
Typer.text = "Hello, world!"

# Typer.repeat_amount = 0
# Typer.key_delay = 0
# Typer.line_delay = 0
# Typer.random_ranges = {"key": [0.05, 0.3], "line": [0.1, 1]}
# Typer.random = False

Typer.start()
```
