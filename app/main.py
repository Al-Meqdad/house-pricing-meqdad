from flask import Flask, jsonify

from src import Prediction_Apis

app = Flask(__name__)

app.register_blueprint(Prediction_Apis.Prediction_Api)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
