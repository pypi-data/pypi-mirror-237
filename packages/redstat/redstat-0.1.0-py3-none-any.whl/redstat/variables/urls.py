BASE_URL = 'https://www.reddit.com/{}'

SUBREDDIT_URL = BASE_URL.format('r/{}.json')
USER_POSTS_URL = BASE_URL.format('user/{}/submitted.json')
USER_COMMENTS_URL = BASE_URL.format('user/{}/comments.json')
