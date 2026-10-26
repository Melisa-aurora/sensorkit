"""Smoothing filters for sampled sensor signals."""


def moving_average(samples, window):
    """Simple moving average; output has len(samples) - window + 1 values."""
    if window <= 0:
        raise ValueError("window must be positive")
    n = len(samples)
    if n < window:
        return []
    out = []
    acc = 0.0
    for i in range(window):
        acc += samples[i]
    out.append(acc / window)
    for i in range(window, n):
        acc += samples[i] - samples[i - window]
        out.append(acc / window)
    return out


def ema(samples, alpha):
    """Exponential moving average with smoothing factor 0 < alpha <= 1."""
    if not 0.0 < alpha <= 1.0:
        raise ValueError("alpha must be in (0, 1]")
    out = []
    if not samples:
        return out
    value = float(samples[0])
    for x in samples:
        value = alpha * x + (1.0 - alpha) * value
        out.append(value)
    return out


def median3(samples):
    """3-point median filter (spike removal); endpoints are kept as-is."""
    n = len(samples)
    out = list(samples)
    for i in range(1, n - 1):
        a = samples[i - 1]
        b = samples[i]
        c = samples[i + 1]
        if a > b:
            a, b = b, a
        if b > c:
            b = c
        if a > b:
            b = a
        out[i] = b
    return out
