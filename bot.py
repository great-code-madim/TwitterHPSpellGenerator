import tweepy
import time

with open("generatedSpells.txt", "r") as f:
    lines = []
    lines = [line.rstrip() for line in f]

with open("pointer.txt", "r") as f:
    pointer = f.readline()

# Can't put the keys on github :/
consumer_key = ''
consumer_secret = ''

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

api.update_status(lines[int(pointer)])

time.sleep(5)

api.update_status(lines[int(pointer) + 1])

time.sleep(5)

api.update_status(lines[int(pointer) + 2])

with open("pointer.txt", "w") as f:
    f.write(str(int(pointer) + 3))
