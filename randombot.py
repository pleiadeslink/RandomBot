from mastodon import Mastodon
import random, os, pathlib

mastodon = Mastodon(
    access_token = 'abcdefg',
    api_base_url = 'https://domain.com/'
)

facts = open(os.path.join(pathlib.Path(__file__).parent.absolute(), 'facts.txt')).read().splitlines()
mastodon.status_post(random.choice(facts))