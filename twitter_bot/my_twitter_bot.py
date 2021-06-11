import tweepy

print('This is my twitter bot')

API_KEY = '4aP9a5QjtkuJCNt0O6lVUSMl1'
API_SECRET_KEY = 'IbpWvYzHkSs65CS9Z5Xs7raoBfd3QjcI1MVooCy9mRfoCe5CRi'
ACCESS_TOKEN = '74996392-be6a2rhOW4tKXAi0IqhboY7XKFPsUwf3AyfL3qby1'
ACCESS_SECRET_TOKEN = 'GqfeYdrujAyxM5UvQp5Ri2vCmGSw60gAimsWmhiciSkQP'
FILE_NAME = 'last_seen_tweet_id.txt'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)
# Get the User object for twitter...
user = api.get_user('twitter')


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_tweet_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_tweet_id


def store_last_seen_id(last_seen_tid, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_tid))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id('last_seen_tweet_id.txt')
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

# 577842483029262336 - use this id for testing
for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.full_text.lower():
        print('found #helloworld in mentions')
        print('responding back...')
        api.update_status('@'+mention.user.screen_name+' HelloWorld back to you !! This is just a test', mention.id)

