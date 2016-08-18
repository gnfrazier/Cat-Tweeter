import time
from twython import Twython


def account_setup():
    app_key = 'MyKey'
    app_secret = 'MySecret'

    oauth_token = "MyToken"
    oauth_token_secret = "MyTokenSecret"

    # Prepare your twitter, you will need it for everything
    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

    return twitter

def tweet(message):
    twitter = account_setup()
    twitter.update_status(status=message)
    time.sleep(5)

def tweet_it(message):
    twitter = account_setup()
    while True:
        try:
            twitter.update_status(status=message)
        except twython.exceptions.TwythonError:
            message = hg_says()
            time.sleep(60)
def main():
    twitter = account_setup()
    twitter.update_status(status="Nap time.")


if __name__ == '__main__':
    main()
