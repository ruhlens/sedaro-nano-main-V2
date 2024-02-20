from flask import Flask
from flask_cors import CORS
from GetData import GetData


app = Flask(__name__)
CORS(app)

@app.route("/")
def postData():
    data = GetData().generateData()
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
