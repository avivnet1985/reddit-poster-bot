
import praw
import time
import logging
from config import reddit_username, reddit_password, client_id, client_secret, user_agent, subreddits, post_title, post_body

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def post_to_reddit():
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=reddit_username,
        password=reddit_password
    )

    for sub in subreddits:
        try:
            reddit.subreddit(sub).submit(post_title, selftext=post_body)
            logger.info(f"✅ Posted to r/{sub}")
            time.sleep(60)
        except Exception as e:
            logger.error(f"⚠️ Error posting to r/{sub}: {e}")
            continue

if __name__ == "__main__":
    post_to_reddit()
