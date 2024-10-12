# create item class that stores an image, description, time and location
import numpy as np
import sqlite3
import pickle

class Item:
    def __init__(self, id:int, image:np.ndarray, emb:np.ndarray, description:str, time:int, location:str):
        self.id = id
        self.image = image
        self.emb = emb
        self.description = description
        self.time = time
        self.location = location
    
    def __str__(self):
        return f'{self.description} found at {self.location} at {self.time}'
    
    def __repr__(self):
        return self.__str__()

class User:
    def __init__(self, username:str, password:str, email:str):
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f'{self.username} with email {self.email}'
    
    def __repr__(self):
        return self.__str__()

class Database:
    def __init__(self):
        self.con = sqlite3.connect('items.db')
        self.cur = self.con.cursor()
        self.create_table()
    
    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, image BLOB, emb BLOB, description TEXT, time INTEGER, location TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, email TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS lost_items (item_id INTEGER, user_id TEXT, PRIMARY KEY (item_id, user_id))')
        self.cur.execute('CREATE TABLE IF NOT EXISTS found_items (item_id INTEGER, user_id TEXT, PRIMARY KEY (item_id, user_id))')
    
    def item_exists(self, id:int) -> bool:
        self.cur.execute('SELECT * FROM items WHERE id = ?', (id,))
        return self.cur.fetchone() is not None

    def insert_item(self, item:Item):
        if self.item_exists(item.id):
            return
        img = item.image.tobytes() if item.image else None
        self.cur.execute('INSERT INTO items (id, image, description, time, location) VALUES (?, ?, ?, ?, ?)', 
                         (item.id, img, item.description, item.time, item.location))
        self.con.commit()
    
    def username_exists(self, username:str) -> bool:
        self.cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.cur.fetchone() is not None
    
    def insert_user(self, user:User):
        self.cur.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (user.username, user.password, user.email))
        self.con.commit()
    
    def authenticate_user(self, username:str, password:str) -> User:
        self.cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = self.cur.fetchone()
        if user:
            return User(*user)
        return None
    
    def insert_lost_item(self, item:Item, user:User):
        self.cur.execute('INSERT INTO lost_items (item_id, user_id) VALUES (?, ?)', (item.id, user.username))
        self.con.commit()
    
    def insert_found_item(self, item:Item, user:User):
        self.cur.execute('INSERT INTO found_items (item_id, user_id) VALUES (?, ?)', (item.id, user.username))
        self.con.commit()
    
    def get_items(self) -> list:
        self.cur.execute('SELECT * FROM items')
        items = self.cur.fetchall()
        return [Item(item[0], pickle.loads(item[1]), pickle.loads(item[2]), item[3], item[4], item[5]) for item in items]
    
    def get_lost_items(self) -> list:
        self.cur.execute('SELECT * FROM lost_items')
        lost_items = self.cur.fetchall()
        return lost_items
    
    def get_found_items(self) -> list:
        self.cur.execute('SELECT * FROM found_items')
        found_items = self.cur.fetchall()
        return found_items
    
    def get_users(self) -> list:
        self.cur.execute('SELECT * FROM users')
        users = self.cur.fetchall()
        return [User(*user) for user in users]
    
    def get_user(self, username:str) -> User:
        self.cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = self.cur.fetchone()
        if user:
            return User(*user)
        return None
    
    def close(self):
        self.con.close()
    