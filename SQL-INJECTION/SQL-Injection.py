from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    #c.execute("CREATE TABLE users (username text, password text)")
    c.execute("SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'")
    user = c.fetchone()
    conn.close()
    if user:
        return 'Welcome, ' + user[0]
    else:
        return 'Login failed'

if __name__ == '__main__':
    # conn = sqlite3.connect('users.db')
    # c = conn.cursor()
    # #c.execute("CREATE TABLE users (username text, password text)")
    # c.execute("INSERT INTO users VALUES ('Hafez', 'Barghouthi')")
    # conn.commit()
    # conn.close()
    app.run(debug=True)
