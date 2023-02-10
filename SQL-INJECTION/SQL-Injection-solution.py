from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    if user:
        return 'Welcome, ' + user[0]
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(debug=True)
