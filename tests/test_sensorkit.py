import binascii

import sensorkit


def test_moving_average():
    assert sensorkit.moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert sensorkit.moving_average([1, 2], 3) == []


def test_ema():
    assert sensorkit.ema([], 0.5) == []
    assert sensorkit.ema([4, 4, 4], 0.3) == [4.0, 4.0, 4.0]


def test_median3():
    assert sensorkit.median3([1, 100, 2, 3, -50, 4]) == [1, 2, 3, 2, 3, 4]


def test_checksums():
    assert sensorkit.crc16_ccitt(b"123456789") == 0x29B1
    data = b"sensor frame"
    assert sensorkit.crc32(data) == binascii.crc32(data)


def test_pid():
    pid = sensorkit.PID(1.0, 0.0, 0.0)
    assert pid.update(0.5, 0.0, 0.1) == 0.5
    assert pid.update(10.0, 0.0, 0.1) == 1.0
