import time
import praw
import regex as re
from pprint import pprint

user_agent = 'KarmaKunt Karma nabbing machine 1.0 by /u/sausagefest2011'
r = praw.Reddit(user_agent=user_agent)

#main running loop
#while True:
subname = u"videos"
sub = r.get_subreddit(subname)
comments = sub.get_comments(limit=None,threshold=2)
count = 0
for comment in comments:
    if comment.score >= 0: #make sure they will like you
        if comment.is_root: #make sure its a top level comment
            #then filter out mentions of subreddits in each comment
            results = [re.sub(ur"\p{P}+", "",word.replace('/r/','')) for word in comment.body.split() if word.startswith('/r/')]
            print results
            count+=1
            if results: #make sure the sub exists
                if subname not in results: #make sure it isn't the same sub
                    print "%s %s" % (subname, results[0]) #make sure to remove punctuation 
                    print "Got a sucker! title is '%s'. \n - checking for subreddit(s) %s..." % (comment.submission, ','.join(results))
                    for result in results:
                        try:
                            r.get_subreddit(result,fetch=True)
                            print " * Sub %s exists!" % result
                        except:
                             print " * Sub %s does not exist.. " % result
print "ran through %i comments" % count

