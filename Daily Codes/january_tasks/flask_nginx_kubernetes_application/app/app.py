from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!! This is integration of flask and Nginx and deployed in kubernetes"

if __name__ == '__main__':
    app.run()