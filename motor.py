import lgpio
import time

h = lgpio.gpiochip_open(0)
MOTOR_PIN = 18
lgpio.gpio_claim_output(h, MOTOR_PIN)

def pfm_run(frequency, duration):
    period = 1.0 / frequency
    half_period = period / 2.0
    start_time = time.time()
    while time.time() - start_time < duration:
        lgpio.gpio_write(h, MOTOR_PIN, 1)
        time.sleep(half_period)
        lgpio.gpio_write(h, MOTOR_PIN, 0)
        time.sleep(half_period)

pfm_run(100, 2)
lgpio.gpiochip_close(h)