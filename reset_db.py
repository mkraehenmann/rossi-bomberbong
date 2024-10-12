from db_manager import *
import os
import yaml

if os.path.exists('items.db'):
    os.remove('items.db')

with open('config_auth.yaml') as f:
    auth = yaml.load(f, Loader=yaml.FullLoader)

users = auth['credentials']['usernames'].keys()
mails = [auth['credentials']['usernames'][user]['email'] for user in users]

db = Database()

for user, mail in zip(users, mails):
    u = User(user, None, mail)
    db.insert_user(u)

print('added users')
print(db.get_users())

db.close()