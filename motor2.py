import time

CHIP = "/sys/class/pwm/pwmchip0"
PWM = f"{CHIP}/pwm0"

STEPS_PER_REV = 200      # đổi theo motor và vi bước
FREQ = 400               # Hz = 400 bước/giây -> 0.5 vòng/giây
REVS = 1                 # số vòng

def write(path, value):
    with open(path, "w") as f:
        f.write(str(value))

try:
    try:
        write(f"{CHIP}/export", 0)
    except OSError:
        pass
    time.sleep(0.2)
    period = int(1e9 / FREQ)
    write(f"{PWM}/duty_cycle", 0)
    write(f"{PWM}/period", period)
    write(f"{PWM}/duty_cycle", period // 2)
    write(f"{PWM}/enable", 1)
    time.sleep(STEPS_PER_REV * REVS / FREQ)   # 200/400 = 0.5 giây
finally:
    write(f"{PWM}/enable", 0)
    write(f"{CHIP}/unexport", 0)
    