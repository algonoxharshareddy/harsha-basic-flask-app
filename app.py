from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello_flask():
    return 'Hello from Docker Flask Application'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')