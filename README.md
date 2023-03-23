# reddit-etl-pipeline

This project demonstrates a simple ETL pipeline to extract data from Reddit, transform the data, and visualize it using Python. 
The extracted data includes information about posts and comments from a specified subreddit.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- `pip` package manager for Python

## Dependencies

This project uses the following libraries:

- `praw` for accessing the Reddit API
- `pandas` for data manipulation
- `matplotlib` for data visualization

To install the required libraries, run the following command:

```bash
pip install praw pandas matplotlib

Here's a README.md template for your project. Replace the placeholders with appropriate information and save this content as README.md in your project's root directory:

markdown
Copy code
# Reddit ETL Pipeline

This project demonstrates a simple ETL pipeline to extract data from Reddit, transform the data, and visualize it using Python. The extracted data includes information about posts and comments from a specified subreddit.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- `pip` package manager for Python

## Dependencies

This project uses the following libraries:

- `praw` for accessing the Reddit API
- `pandas` for data manipulation
- `matplotlib` for data visualization

To install the required libraries, run the following command:

```bash
pip install praw pandas matplotlib


Reddit API Credentials
You need to have Reddit API credentials to run this project. If you don't have them, follow these steps:

Go to https://www.reddit.com/prefs/apps.
Click on the "Create App" or "Create Another App" button.
Fill out the form with the following details:
"name": Enter a name for your application.
"App type": Choose "script".
"description": Enter a brief description (optional).
"about url": Leave this field blank.
"redirect uri": Enter "http://localhost:8080" (without quotes).
"permissions": Leave this as default.
Click "Create app" or "Update app".
Note down the "client ID" (the string under the app name) and the "client secret".


Usage
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/dhrumilsindhwa/reddit-etl-pipeline.git
Navigate to the project directory:
bash
Copy code
cd reddit-etl-pipeline
Open the main script (your_script_name.py) in your favorite text editor, and replace the placeholder values for client_id, client_secret, and user_agent with your Reddit API credentials.

Run the script:

bash
Copy code
python your_script_name.py
This will extract data from the specified subreddit, transform it, and generate two visualizations: a bar chart of the top 10 posts by score and a pie chart showing the distribution of comments among the top 10 posts.
