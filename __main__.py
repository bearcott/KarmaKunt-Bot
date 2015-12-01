import time
import praw
import regex as re
from pprint import pprint
import config
import webbrowser

user_agent = 'KarmaKunt Karma nabbing machine 1.0 by /u/sausagefest2011'
r = praw.Reddit(user_agent=user_agent)

#set up Oauth for account
r.set_oauth_app_info(client_id=config.ID,
                     client_secret=config.SECRET,
                     redirect_uri='http://127.0.0.1:%s/authorize_callback'%(config.PORT))

url = r.get_authorize_url('RandDdoMaskShitStrkingFurU.Haxkor!', 'identity', True)
webbrowser.open(url)


#main running loop
#while True:
subname = u"videos"
sub = r.get_subreddit(subname)
comments = sub.get_comments(limit=None,threshold=2)
count = 0

def fetch_auth_token():
    return true

def autheticating_server(BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', config.PORT)
    while fetch_auth_token():
        httpd.handle_request()

def authenticate:
    httpd = BaseHTTPServer.HTTPServer(server_address,authenticating_server(BaseHTTPServer.BaseHTTPRequestHandler)
    
        
    

for comment in comments:
    if comment.score >= 0: #make sure they will like you
        if comment.is_root: #make sure its a top level comment
            #then filter out mentions of subreddits in each comment
            results = [re.sub(ur"\p{P}+", "",word.replace('/r/','')) for word in comment.body.split() if word.startswith('/r/')]
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

