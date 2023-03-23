import matplotlib.pyplot as plt
from extract import get_subreddit_data, transform_data

def plot_top_posts(top_posts):
    plt.figure(figsize=(12, 6))
    plt.barh(top_posts['title'], top_posts['score'])
    plt.xlabel('Upvotes')
    plt.ylabel('Post Title')
    plt.title('Top 5 Posts by Score')
    plt.gca().invert_yaxis()
    plt.show()

def plot_comments_distribution(top_posts):
    plt.figure(figsize=(8, 8))
    plt.pie(top_posts['num_comments'], labels=top_posts['title'], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Number of Comments Distribution Among Top 5 Posts')
    plt.show()  # Add this line to display the pie chart


if __name__ == "__main__":
    subreddit = "dataengineering"  # Replace with the desired subreddit
    post_limit = 100

    df = get_subreddit_data(subreddit, post_limit)
    top_posts, avg_num_comments = transform_data(df)

    plot_top_posts(top_posts)
    plot_comments_distribution(top_posts)

    print(f"Average number of comments: {avg_num_comments:.2f}")
