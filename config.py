import os


class TwitterConfig:
    CONSUMER_KEY = os.environ.get('O076uiBWnTLGRt7OMAd4jVZl6')
    CONSUMER_SECRET = os.environ.get('L8tvPCxkI0GjzRdDyS7ubIUpy9Da1wts5WpJXC0wmfjXezYnWC')
    ACCESS_TOKEN = os.environ.get('933740502549229568-xnjJLLfY9jHhxUWczGBV92HBUV4PVBw')
    ACCESS_TOKEN_SECRET = os.environ.get('3ztfhPkOQ5CnMQqNNRlaXce1xsOA5ofScqcIexIPG1rzA')


class DBConfig:
    USER = os.environ.get('twitterscript')
    PWORD = os.environ.get('Argonek.007')
    HOST = os.environ.get('DESKTOP-HS4CRAC')


if __name__ == '__main__':
    print(type(os.environ.get('CONSUMER_KEY')))


