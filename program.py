#!/usr/share/python3
import random
import statistics
import arrow as arrow
import detect
import time
import notify
import dblog

tlist = []
triglist = []


def calibrate():
    print('Calibrating...')
    dist = detect.take_reading()
    distlist = [dist]

    for i in range(3):
        dist = detect.take_reading()

        distlist.append(dist)

    cal_number = round(statistics.mean(distlist), 3)
    cal_time = arrow.now()
    print('Calibration Complete, number is {} cm at {}'.format(cal_number, cal_time))
    cal_time = arrow.now().float_timestamp
    dblog.cal_log(cal_time, cal_number)
    return cal_number


def hg_says():
    sayings = ["Meow",
               "I'm home now!",
               "I can see you in there, let me in.",
               "Hey, can a poor hungry cat get some food?",
               "I met a bird this morning, I called it Breakfast.",
               "I brought you a present, it is on the doormat.",
               "Time for a nap.",
               "Squirrel!",
               "Let me in now, or the flowerbed gets it.",
               "I think I will call you 'lunch'. Hello lunch!",
               "That shoelace had it coming.",
               "Only 14 hours sleep today, I am exhausted.",
               "I don't know what that was but it was furry and delicious.",
               "Purrrrr",
               "Meoowwwwwerrrrr"
               ]

    quote = sayings[random.randint(0, (len(sayings) - 1))]

    return quote


def sensorlog(trig_dist):
    if max(trig_dist) - min(trig_dist) < 2:
        calibrate()
        trig_dist = []

    else:
        for i in range(10):
            del trig_dist[0]

    return trig_dist


def counter(dist):
    home = False
    counter_time = arrow.now().float_timestamp
    dblog.detect_log(counter_time, dist)
    tlist.append(counter_time)

    if len(tlist) == 5:
        tspan = tlist[-1] - tlist[0]
        if tspan < 6.9:
            print(tspan, " Hg is Home!")
            dblog.trigger_log(counter_time)
            home = True

        del tlist[0]

    return home


def report(tweetlog):
    tstamp = arrow.now()

    if tweetlog + 300 < arrow.now().float_timestamp:
        status = hg_says()
        # notify.tweet_it(message=status)  # comment out during debug!
        print('Catalarm is in Debug mode, status message would have been:    {} at {}'.format(status, tstamp))
        dblog.tweet_log(tweetlog, status)
        time.sleep(10)  # removed to keep logging detections while not triggering messages
        tweetlog = arrow.now().float_timestamp

    return tweetlog


def main():
    tweetlog = arrow.now().float_timestamp
    dblog.start_log(tweetlog)
    cal = calibrate()
    elog = 0
    trig_dist = []

    for i in range(606000):
        dist = detect.take_reading()
        # if return is 6cm less than cal then fire counter

        if dist < (cal - 6):
            trig_dist.append(dist)
            home = counter(dist)  # if counter is more than 5 triggers
            #  in 7 seconds then return True

            if home:
                tweetlog = report(tweetlog)
                time.sleep(3)

        elif dist > (cal + 4):
            elog += 1

            if elog == 10:
                cal = calibrate()
                elog = 0

            elif elog > 11:
                status = str("Something has gone wrong.")
                print(status)
                # notify.tweet(status) #comment out during debug

        elif len(trig_dist) > 120:
            trig_dist = sensorlog(trig_dist)

        else:
            status = str("I don't see Hg.")


if __name__ == '__main__':
    main()
