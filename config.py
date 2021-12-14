import os
from dotenv import load_dotenv
load_dotenv()

# I am introducing dotenv because I found it to be the easiest way to set config file up.
# You can check if this is working through according python commands eg print(USER)

class TwitterConfig:
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


class DBConfig:
    USER = os.environ.get('DB_USER')
    PWORD = os.environ.get('DB_PWORD')
    HOST = os.environ.get('DB_HOST')
    PORT = os.environ.get('DB_PORT')


if __name__ == '__main__':
    print(type(os.environ.get('CONSUMER_KEY')))
