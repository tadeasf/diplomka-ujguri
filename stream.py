from database import session_scope, init_db
from models import Tweet
from tweepy.streaming import StreamListener
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

logger = logging.getLogger(__name__)


class TweetListener(StreamListener):

    def __init__(self, keywords):
        StreamListener.__init__(self)
        init_db()
        self.keywords = keywords
        self.sentiment_model = SentimentIntensityAnalyzer()

    def on_status(self, status):
        if status.retweeted or 'RT @' in status.text:
            return
        if status.truncated:
            text = status.extended_tweet['full_text']
        else:
            text = status.text
            # this is where I can try to implement spelling correction later
        keyword = self.check_keyword(text)
        if not keyword:
            return
        sentiment = self.sentiment_model.polarity_scores(text).get('compound')
        if sentiment == 0:
            return
        tweet = Tweet(body=text, keyword=keyword, tweet_date=status.created_at, followers=status.user.followers_count,
                      tweetid=status.id, userid=status.user.id, tweetsource=status.source, sentiment=sentiment)
        self.insert_tweet(tweet)
        # Huge changes here! I got rid of location. Only a handful of tweets have it, I read through all API options and there isn't a nice way to get it in readytobeplotted format
        # I included user ID (I can trace tweets back now if I will want to! (which is great for metric-lookup in the future)
        # Also newly included: tweet ID (I can trace back tweets) and source of the tweets. Might be interesting metric in the future

    def on_error(self, status_code):
        if status_code == 420:
            # Stream limit reached, need to close the stream
            logger.warning('Limit Reached. Closing stream ({})'.format(self.lead_keyword))
            return False
        logger.warning('Streaming error (status code {})'.format(status_code))

    def insert_tweet(self, tweet):
        try:
            with session_scope() as sess:
                sess.add(tweet)
        except Exception as e:
            logger.warning('Unable to insert tweet: {}'.format(e))

    def check_keyword(self, body):
        for keyword in self.keywords:
            if keyword in body:
                return keyword
        return None

