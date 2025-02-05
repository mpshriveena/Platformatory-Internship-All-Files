from flask import Flask, request
import urllib.parse
app = Flask(__name__)
@app.route('/get-spanish-greeting', methods=['GET'])
def get_spanish_greeting():
    name = request.args.get('name', '')
    return f"Hola, {name}!"
if __name__ == '__main__':
    app.run(host='localhost', port=9999)