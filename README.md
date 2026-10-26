# sensorkit

Plain-Python signal-processing helpers for sensor data, with a configuration
that cythonizes them for **armv8-a (aarch64 Linux)**.

| Module | Contents |
|---|---|
| `sensorkit/filters.py` | `moving_average`, `ema`, `median3` |
| `sensorkit/checksum.py` | `crc16_ccitt`, `crc32` |
| `sensorkit/control.py` | `PID` controller |

## Cythonization config

`setup.py` is the cythonization configuration:

- `CYTHON_MODULES` - modules compiled to native extensions (`.py` -> `.c` -> `.so`)
- `CYTHON_DIRECTIVES` - Cython compiler directives
- `ARMV8_CFLAGS` - C flags for the armv8 target (`-march=armv8-a -O2`)

The repository contains only Python sources; nothing is pre-built.

## Building

On aarch64 Linux (or with an aarch64 cross toolchain):

```bash
pip install "Cython>=3.0" setuptools wheel
python setup.py build_ext --inplace
```

Result: `src/sensorkit/{filters,checksum,control}.cpython-3XX-aarch64-linux-gnu.so`.

## Tests

```bash
PYTHONPATH=src python -m pytest tests
```
