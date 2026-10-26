"""sensorkit - small signal-processing helpers for sensor data."""

from sensorkit.filters import moving_average, ema, median3
from sensorkit.checksum import crc16_ccitt, crc32
from sensorkit.control import PID

__all__ = ["moving_average", "ema", "median3", "crc16_ccitt", "crc32", "PID"]
__version__ = "0.1.0"
