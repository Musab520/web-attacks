from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    csrf_token = generate_csrf_token()
    return render_template('index.html', csrf_token=csrf_token)

@app.route('/transfer', methods=['POST'])
def transfer():
    if request.form.get('csrf_token') != generate_csrf_token():
        return 'Invalid CSRF token'
    amount = request.form.get('amount')
    return f'Transferred {amount}'

def generate_csrf_token():
    return 'secret-token'

if __name__ == '__main__':
    app.run(debug=True)
