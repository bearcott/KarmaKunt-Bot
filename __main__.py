import time
import praw
from pprint import pprint

user_agent = 'KarmaKunt Karma nabbing machine 1.0 by /u/sausagefest2011'
r = praw.Reddit(user_agent=user_agent)

#main running loop
#while True:
sub = r.get_subreddit("videos")
comments = praw.helpers.flatten_tree(sub.get_comments())
for comment in comments:
    results = [word for word in comment.body.split() if word.startswith('/r/')]
    pprint(results)    
    #time.sleep(10)

