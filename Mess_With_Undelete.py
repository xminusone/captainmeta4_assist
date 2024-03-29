#This is a script that can be run in order to generate false submissions on /r/undelete
#This script exists for the sole purpose of assholery.
#Requires that you have posts permissions in all subreddits that you moderate

import praw
import time

r=praw.Reddit("Undelete Garbage Generator v1 by /u/captainmeta4")
r.login(input("Username: "), input("Password: "))

#Get a list of subs that the user moderates
my_moderation=[]
for subreddit in r.get_my_moderation(limit=1000):
    my_moderation.append(subreddit)
    
#Load the top 1000 submissions from /r/all/hot and make a listing of submissions that I can remove
posts = []
print("Checking /r/all for submissions you can remove")
i=0
for submission in r.get_subreddit('all').get_hot(limit=100):
    i=i+1
    print(str(i)+"/100")
    if submission.subreddit in my_moderation:
        posts.append(submission.fullname)

num=len(posts)   
print("Found "+str(num)+" usable submissions")
print("Removing posts...")

#Remove all the posts
i=0
for submission in r.get_info(thing_id=posts):
    i=i+1
    print(str(i)+'/'+str(num))
    submission.remove()

print("posts removed")
print("Waiting 30 seconds")

time.sleep(30)

#And put all the posts back up
print("Restoring posts...")
i=0
for submission in r.get_info(thing_id=posts):
    i=i+1
    print(str(i)+'/'+str(num))
    submission.approve()

print("posts restored")
