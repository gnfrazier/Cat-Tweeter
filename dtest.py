import RPi.GPIO as GPIO
import time


def take_reading():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    trig = 24
    echo = 23

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, False)
    time.sleep(1)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    pulse_start = 0
    pulse_end = 0

    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = round((pulse_duration * 17150), 1)

    # print(distance, "cm")

    GPIO.cleanup()

    return distance

if __name__ == '__main__':

    for i in range(500):
        take_reading()
