from flask import Flask, request
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if not re.match(r'^https?://', url):
        return 'Invalid URL'
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
