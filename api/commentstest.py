import scratchattach as sb3

user = sb3.get_project(908857043)
comments = user.comments(limit=999, offset=0)

for comment in comments:
    print(comment['author']['username'])
    print(comment['content'])
    for reply in user.get_comment_replies(comment_id=comment['id'], limit=999, offset=0):
        print(reply['author']['username'])
        print(reply['content'])