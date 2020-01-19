from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))

if __name__ == '__main__':
    app.run(port=7000)