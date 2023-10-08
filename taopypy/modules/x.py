import tweepy


def do_tweet(
    consumer_key: str,
    consumer_secret: str,
    access_token: str,
    access_token_secret: str,
    share_content_list: list,
) -> list:
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    for content in share_content_list:
        client.create_tweet(text=f"{content['title']}\n\n{content['url']}")

    return share_content_list
