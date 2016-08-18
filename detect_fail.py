import RPi.GPIO as GPIO
import time


#def set_pins():
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN)

    #return (trig, echo)


def dist():
    #echo = pins[1]
    #trig = pins[0]
    GPIO.output(trig, False)
    time.sleep(0.3)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    pulse_start = 0
    pulse_end = 0

    while GPIO.input(echo) == False:
        pulse_start = time.time()

    while GPIO.input(echo) == True:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    print(pulse_duration)

    distance = round((pulse_duration * 17150), 2)

    print(distance)

    return distance


def main():
    pins = set_pins()

    for i in range(2):

        distance = dist(pins)

        while distance > 1000:
            time.sleep(0.2)
            distance = dist(pins)

        print('Detect ended with a distance of {}.'.format(distance))


if __name__ == '__main__':
    main()
