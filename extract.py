import praw
import pandas as pd

# Replace with your Reddit API credentials
client_id = '95vPNiPwbssQsqtQoseTmA'
client_secret = '9bLzJbkJ7ZZdOLbXbGO5PBdcwszFGg'
user_agent = 'son_of_sisyphos'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

def get_subreddit_data(subreddit, post_limit=100):
    subreddit_data = reddit.subreddit(subreddit)
    posts = []

    for post in subreddit_data.hot(limit=post_limit):
        post_data = {
            'title': post.title,
            'score': post.score,
            'id': post.id,
            'url': post.url,
            'num_comments': post.num_comments,
            'created': pd.to_datetime(post.created_utc, unit='s'),
            'author': post.author.name if post.author else 'N/A'
        }
        posts.append(post_data)

    df = pd.DataFrame(posts)
    return df

def transform_data(df):
    # Sort by score and select the top 10 posts
    top_posts = df.sort_values(by='score', ascending=False).head(5)

    # Calculate the average number of comments
    avg_num_comments = df['num_comments'].mean()

    return top_posts, avg_num_comments
