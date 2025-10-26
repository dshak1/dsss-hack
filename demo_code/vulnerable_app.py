
# Vulnerable application - DO NOT USE IN PRODUCTION
import sqlite3
import hashlib

def login(username, password):
    # SQL INJECTION VULNERABILITY
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect('users.db')
    return conn.execute(query).fetchone()

def hash_password(password):
    # WEAK CRYPTOGRAPHY - MD5 is broken
    return hashlib.md5(password.encode()).hexdigest()

# HARDCODED CREDENTIALS
API_KEY = "sk-1234567890abcdef"
SECRET_PASSWORD = "admin123"

def render_user_input(user_input):
    # XSS VULNERABILITY
    return f"<div>Welcome {user_input}!</div>"

def read_file(filename):
    # PATH TRAVERSAL VULNERABILITY
    with open(filename, 'r') as f:
        return f.read()
