"""Discrete PID controller."""


class PID:
    """PID controller with output clamping and integral anti-windup."""

    def __init__(self, kp, ki, kd, out_min=-1.0, out_max=1.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.out_min = out_min
        self.out_max = out_max
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint, measured, dt):
        """Advance one step of length dt and return the clamped output."""
        if dt <= 0.0:
            raise ValueError("dt must be positive")
        error = setpoint - measured
        integral = self.integral + error * dt
        derivative = (error - self.prev_error) / dt
        out = self.kp * error + self.ki * integral + self.kd * derivative
        if out > self.out_max:
            out = self.out_max
        elif out < self.out_min:
            out = self.out_min
        else:
            self.integral = integral
        self.prev_error = error
        return out
