from tinydb import TinyDB, Query

db = TinyDB('db.json')


def start_log(tweetlog):
    db.insert({'Activity': 'Start-Up', 'Time': tweetlog})


def cal_log(cal_time, cal_number):
    db.insert({'Activity': 'Calibration', 'Time': cal_time, 'Distance': cal_number})


def detect_log(detect_time, dist):
    db.insert({'Activity': 'Detection', 'Time': detect_time, 'Distance': dist})


def trigger_log(counter_time, ):
    db.insert({'Activity': 'Trigger', 'Time': counter_time})


def tweet_log(tweet_time, message):
    db.insert({'Activity': 'Tweet', 'Time': tweet_time, 'Message': message})


def main():
    start_log('dblog run')


if __name__ == '__main__':
    main()
