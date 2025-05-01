import sqlite3
import bcrypt

def migrate():
    conn = sqlite3.connect('velocity.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES users(id),
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS privatemessages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES users(id),
            FOREIGN KEY (receiver_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_message(sender_id, message):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (sender_id, message)
        VALUES (?, ?)
    ''', (sender_id, message))
    conn.commit()
    conn.close()

def add_private_message(sender_id, receiver_id, message):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO privatemessages (sender_id, receiver_id, message)
        VALUES (?, ?, ?)
    ''', (sender_id, receiver_id, message))
    conn.commit()
    conn.close()

def verify_password(username, password):
    user = get_user(username)
    if user:
        stored_password = user[2]
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    return False

def fetch_messages(start_index):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM messages 
        ORDER BY timestamp DESC 
        LIMIT 10 OFFSET ?
    ''', (start_index,))
    messages = cursor.fetchall()
    conn.close()
    return messages

def fetch_private_messages(sender_id, receiver_id, start_index):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM privatemessages 
        WHERE sender_id = ? AND receiver_id = ? 
        ORDER BY timestamp DESC LIMIT 10 OFFSET ?
    ''', (sender_id, receiver_id, start_index))
    messages = cursor.fetchall()
    conn.close()
    return messages

def get_user_by_id(user_id):
    conn = sqlite3.connect('velocity.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user