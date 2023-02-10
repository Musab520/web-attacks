from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="http://localhost:5000/transfer" method="post">
            <input type="text" name="amount">
            <input type="submit" value="Transfer">
        </form>
    '''

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form.get('amount')
    return f'Transferred {amount}'

if __name__ == '__main__':
    app.run(debug=True)