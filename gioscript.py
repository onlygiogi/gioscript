"""
This script is written by @gioggino:
- GitHub: https://github.com/gioggino/
- Instagram: https://www.instagram.com/giogginodev/
"""

# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'username'
insta_password = 'password'

# friends you don't want to interact with (only like)
friends_list = []

# account you want to ignore
ignore_list = []

# hastags you don't want to interact with
dont_like_tag_list = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
                      'egg', 'chicken', 'cheese', 'sausage', 'lobster',
                      'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
                      'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
                      'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
                      'protein', 'essen', 'mahl', 'breakfast', 'lunch',
                      'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
                      'sushi', 'burger', 'salmon', 'shrimp', 'steak',
                      'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
                      'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
                      'breakfast', 'dinner', 'lunch']

# hastags you want to interact with
like_tag_list = []

# accounts with similar contents
accounts = []

# location of the page
location = []

# comments
photoComments = [u'Good Photo :thumbsup:! @{}']
videoComments = [u'Great Video :thumbsup:! @{}']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  nogui=True,
                  disable_image_load=True,
                  bypass_security_challenge_using='email')  # email/sms

# let's go! :>
with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(friends_list)
    session.set_ignore_if_contains(ignore_list)
    session.set_dont_like(dont_like_tag_list)
    session.set_comments(photoComments, media='Photo')
    session.set_comments(videoComments, media='Video')
    # premium settings
    session.set_relationship_bounds(enabled=False,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=999999999999,
                                    min_followers=50,
                                    max_following=50,
                                    min_following=50,
                                    max_post=50,
                                    min_post=50,)
    session.set_skip_users(skip_private=True,
                           private_percentage=100,
                           skip_no_profile_pic=False,
                           no_profile_pic_percentage=100,
                           skip_business=False,
                           skip_non_business=False,
                           business_percentage=100,)
    session.set_delimit_liking(
        enabled=False, max_likes=1005, min_likes=20)
    session.set_delimit_commenting(
        enabled=False, max_comments=32, min_comments=0)

    # sleep rules (anti-ban)
    session.set_action_delays(enabled=True,
                              like=3,
                              comment=5,
                              follow=3,
                              unfollow=28,
                              story=10,
                              randomize=True, random_range_from=70, random_range_to=140)

    # quota supervisor (anti-ban)
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows"],
                                 peak_likes_hourly=100,
                                 peak_comments_hourly=50,
                                 peak_follows_hourly=200)

    # interactions
    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)
    session.set_do_story(enabled=True, percentage=70, simulate=False)

    # activity
    session.follow_user_followers(accounts, amount=800,
                                  randomize=False, interact=False)

    # by tags
    session.follow_by_tags(like_tag_list, amount=10)
    session.like_by_tags(like_tag_list, amount=800,
                         randomize=False, interact=False)

    # by location (optional)
    session.follow_by_locations(location, amount=800)
    session.like_by_locations(location, amount=800)

    # comments
    session.set_do_comment(enabled=True, percentage=25)

    # watch up to 20 stories published with specified tags (optional)
    session.story_by_tags(like_tag_list)

    # unfollow
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)
