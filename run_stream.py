import os, logging, datetime, argparse
from logging.handlers import RotatingFileHandler
from stream import TweetListener
from tweepy import Stream
from tweepy import OAuthHandler
from urllib3.exceptions import ProtocolError
from config import TwitterConfig

log_dir = 'Logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_name = 'streaming_{}.log'.format(datetime.date.today().strftime('%Y%m%d'))
log_handler = RotatingFileHandler(filename=os.path.join(log_dir, log_name), maxBytes=20000, backupCount=5)
logging.basicConfig(handlers=[log_handler], level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt='%Y-%m-%dT%H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser(description='Database twitter streams.')
    parser.add_argument("-k", "--keywords", type=str, required=True,
                        help="Keywords to filter stream (comma seperated, wrap in quotation marks")
    args = parser.parse_args()
    return args



auth = OAuthHandler(TwitterConfig.CONSUMER_KEY, TwitterConfig.CONSUMER_SECRET)
auth.set_access_token(TwitterConfig.ACCESS_TOKEN, TwitterConfig.ACCESS_TOKEN_SECRET)
keywords = parse_args().keywords.split(',')
keywords = [word.strip(' ') for word in keywords]
listener = TweetListener(keywords)


def start_stream():
    while True:
        try:
            stream = Stream(auth, listener)
            logging.info('Starting stream: {}'.format(keywords[0]))
            stream.filter(track=keywords, languages=['en'], stall_warnings=True)
            logging.info('Stream closed')
        except:
            continue
# Neat little infinity while loop. I'm not getting the errors but at this point, I had the script running for 24 hours almost and connection breaks happen due to regular stuff. Reconnecting is always wanted
# This could change when I'm going to be implementing further work to on_stream function


if __name__ == '__main__':
    start_stream()

