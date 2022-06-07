import praw 
from praw.models import MoreComments
import pandas as pd

url = "https://www.reddit.com/r/ask/comments/r8n9i8/why_did_you_stop_using_facebook"

# read only praw instance 
r = praw.Reddit(client_id="45bl1Dce-rpqMwRa1UecZA",
                client_secret="M0iq4f-qsmTr3y_jtMAK75CuxwngxA",
                user_agent="Wistoft2410")

# change the url variable to the given submission (subreddit post) that you want
submission = r.submission(url = url)
subreddit = r.subreddit("ask") # locating the subreddit that I'm interested in scraping 

# technical data 
print("reddit object: ", type(r))
print("subreddit post object",type(submission.comments),"\n")

# domain insight : 
print("subreddit titel: ", subreddit)
print("submission url: ", submission.url)
print("submission author: ", submission.author)


# practical information about the subreddit post
print("submission id: ", submission.name, "\n")
print("total comments: ", submission.num_comments)
print("total score: ", submission.score, "\n")


'''
# displaying specific data been located  
print("Display Name: ", subreddit.display_name)
print("Titel: ", subreddit.title)
print("Description:", subreddit.description)
'''

'''
# testing 
hot_posts = r.subreddit('ask').hot(limit=10)
print("hot posts: ", hot_posts)
'''

print("check point 1")

num = 0
comment_dict = []
# fetching all the relevant comments
for top_submission_comments in submission.comments:
    if isinstance(top_submission_comments, MoreComments):
        continue
    num += 1
    print(".................................","\n")
    print("com num: ", num)
    print("user id: ",top_submission_comments.id)
    print("parent id:",top_submission_comments.parent_id,"\n")
    
    print(top_submission_comments.body)  

    # appending 
    comment_dict.append(top_submission_comments.body)
    pass


print("check point 2: ", "total comments: ", num)
print("check point 2: ", "total comments: ", comment_dict)

# testing 
print(com_dict)

# create pandas raw dataframe
df = pd.DataFrame(com_dict)

# skip first row due to invalid 'bot' commment
df = df.iloc[1: , :] 
df

# adjust this variable to be either '1' or '0' in relation to export format for the dataframe
csv_or_not = 1

if csv_or_not == 0: 
    file_name = 'subreddit_data_3.xlsx' 
    df.to_excel(file_name)
    
elif csv_or_not == 1:
    file_name = 'subreddit_data_3.csv'
    df.to_csv(file_name)
