# sensorkit

Plain-Python signal-processing helpers for sensor data, with a configuration
that cythonizes them into native extensions.

| Module | Contents |
|---|---|
| `sensorkit/filters.py` | `moving_average`, `ema`, `median3` |
| `sensorkit/checksum.py` | `crc16_ccitt`, `crc32` |
| `sensorkit/control.py` | `PID` controller |

## Cythonization config

`setup.py` is the cythonization configuration:

- `CYTHON_MODULES` - modules compiled to native extensions (`.py` -> `.c` -> `.so`)
- `CYTHON_DIRECTIVES` - Cython compiler directives

The repository contains only Python sources; nothing is pre-built.

## Building

```bash
pip install "Cython>=3.0" setuptools wheel
python setup.py build_ext --inplace
```

Result: one native extension per module in `src/sensorkit/` (`filters`, `checksum`, `control`).

## Tests

```bash
PYTHONPATH=src python -m pytest tests
```
