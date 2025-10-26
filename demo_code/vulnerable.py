# Vulnerable code - DO NOT USE IN PRODUCTION
import sqlite3
import hashlib

def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return sqlite3.connect('users.db').execute(query).fetchone()

API_KEY = "sk-1234567890"
password = "admin123"
