from flask import Flask, jsonify

from Prediction_Apis import Prediction_Api
app = Flask(__name__)

app.register_blueprint(Prediction_Api)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
