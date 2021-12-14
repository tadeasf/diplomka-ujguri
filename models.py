from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from database import Base


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    body = Column(String(1000), nullable=False)
    keyword = Column(String(256), nullable=False)
    tweet_date = Column(DateTime, nullable=False)
    followers = Column(Integer)
    tweetid = Column(String(100))
    userid = Column(String(100))
    tweetsource = Column(String(100))
    sentiment = Column(Float)
# Again, I changed my SQL database accordingly so data can be written properly
# Nothing to scientific here. You can find classes of twitter api arguments in twitter documentation

    def __init__(self, body, keyword, tweet_date, followers, tweetid, userid, tweetsource, sentiment):
        self.body = body
        self.keyword = keyword
        self.tweet_date = tweet_date
        self.followers = followers
        self.tweetid = tweetid
        self.userid = userid
        self.tweetsource = tweetsource
        self.sentiment = sentiment

    def __repr__(self):
        return '<Tweet %r>' % self.body
