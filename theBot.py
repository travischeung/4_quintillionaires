from instapy import InstaPy
from instapy import smart_run
import json

# imports user data (for security purposes kept separate)
f = open("user_pass.json", 'r')
userData = json.loads(f.read())
print(userData.get("username"))
print(userData.get("password"))
# hopefully this will sign me in
# session = InstaPy(username = userData.get("username"), password = userData.get("password"))
session = InstaPy(username=userData.get("username"),
                  password=userData.get("password"),
                  geckodriver_path='C:\\Users\\Lok PC\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe')
# session.login()
with smart_run(session):
    # begin the epic motivation
    session.set_do_follow(enabled=True, percentage=100)
    session.set_comments(["follow me for epic tips to be quintillionaire"])
    session.set_do_comment(enabled=True, percentage=100)
    session.interact_by_users(['ishaucerous'],amount=5,randomize=False,media="Photo")
