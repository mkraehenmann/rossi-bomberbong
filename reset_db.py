from db_manager import *
import os
import yaml

# read users from config_auth.yaml
with open('config_auth.yaml') as f:
    auth = yaml.load(f, Loader=yaml.FullLoader)
users = auth['credentials']['usernames'].keys()
mails = [auth['credentials']['usernames'][user]['email'] for user in users]

# recreate database
if os.path.exists('items.db'):
    os.remove('items.db')
db = Database()

# populate users
users_tmp = []
jsmith_index = 0
for user, mail in zip(users, mails):
    if user == 'jsmith':
        jsmith_index = len(users_tmp)
    u = User(user, None, mail)
    db.insert_user(u)
    users_tmp.append(u)
print('added users')

# populate items
description = 'lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. lore ipsum dolor sit amet, consectetur adipiscing elit. '
items = [
    Item(10, None, None, description, 0, 'b'),
    Item(11, None, None, description, 1, 'd'),
    Item(12, None, None, description, 2, 'f'),
    Item(13, None, None, description, 3, 'h'),
]
for item in items:
    db.insert_item(item)
print('added items')

# populate lost found
db.insert_lost_item(items[0], users_tmp[jsmith_index])
db.insert_lost_item(items[1], users_tmp[jsmith_index])
db.insert_found_item(items[2], users_tmp[jsmith_index])
db.insert_found_item(items[3], users_tmp[jsmith_index])
print('added lost found')

# populate matches
db.insert_match(12, 10)
print('added matches')

# close database
db.close()