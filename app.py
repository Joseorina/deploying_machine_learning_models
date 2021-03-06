from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def add():
   a = request.form['a']
   b = request.form['b']
   return str(int(a) + int(b))

def predict(house_size, house_beds):
    prediction = ml_model.predict(house_price, house_beds)
    return prediction

if __name__ == '__main__':
    app.run(port=7000)