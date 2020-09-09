from instapy import InstaPy
from instapy import smart_run
import json

# imports user data (for security purposes kept separate)
f = open("user_pass.json", 'r')
userData = json.loads(f.read())
print(userData.get("username"))
print(userData.get("password"))
# hopefully this will sign me in
currSession = InstaPy(username = userData.get("username"), password = userData.get("password"),headless_browser=False)

with smart_run(session):
    # begin the epic motivation
    session.set_do_follow(enabled=True, percentage=50)
    session.set_comments(["follow me for epic tips to be quintillionaire"])
    session.set_do_comment(enabled=True, percentage=100)
    session.interact_by_users(['chilltravischill'])


    # session.set_do_follow(enabled=False, percentage=50)
    # session.set_comments(["Cool", "Super!"])
    # session.set_do_comment(enabled=True, percentage=80)
    # session.set_do_like(True, percentage=70)
    # session.interact_by_users(['user1', 'user2', 'user3'], amount=5, randomize=True, media='Photo')