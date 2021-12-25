from flask import Flask, jsonify
import os
from src import Prediction_Apis

app = Flask(__name__)

app.register_blueprint(Prediction_Apis.Prediction_Api)
PORT = 4000
if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', 5000), host="0.0.0.0")
