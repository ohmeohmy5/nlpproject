import praw

reddit = praw.Reddit(client_id = 'gRXjQD0nWFOlTg',
                     client_secret = 'bnSAFSFj1mb-z_8nY5_W7bwc22k',
                     username = 'ohmeohmy5',
                     password = 'thereads5',
                     user_agent = 'nlpprojectv1')

subreddit = reddit.subreddit('investing')