import time
import praw
from pprint import pprint

user_agent = 'KarmaKunt Karma nabbing machine 1.0 by /u/sausagefest2011'
r = praw.Reddit(user_agent=user_agent)

#main running loop
#while True:
subname = "videos"
sub = r.get_subreddit(subname)
comments = praw.helpers.flatten_tree(sub.get_comments())
r.get_subreddit("lmao",fetch=True)
for comment in comments:
    results = [word for word in comment.body.split() if word.startswith('/r/')]
    if results:
        if any(subname not in result for result in results):
            pprint(results)
            print comment.title
    #time.sleep(10)

