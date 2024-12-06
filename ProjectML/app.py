
from flask import Flask
from controller.predict import predict
app = Flask(__name__)

@app.post('/api/v1/predict')
def post_user():
    return predict()

@app.get('/test')
def test():
    return "halo"

if __name__ == '__main__':
    app.run(debug=True)