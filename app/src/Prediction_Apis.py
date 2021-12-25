from flask import request, jsonify, Blueprint
import pickle
import pandas as pd
from flask_expects_json import expects_json
from typing import Any
from io import StringIO
from werkzeug.wrappers import Response
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def get_data(json_object):
    Object = json_object.keys()
    temp = []
    columns = []
    for key in Object:
        temp.append(json_object[key])
        columns.append(key)

    data_frame = pd.DataFrame([temp], columns=columns)
    return data_frame


def stringifydata(patch_file):
    data = []
    for x in patch_file:
        data.append(str(x[0])+"\n")

    return data


Prediction_Api: Blueprint = Blueprint(
    'Prediction_Api', __name__, url_prefix='/api/v1')


pipeline: Pipeline

single_prediction_jsonschema = {
    'type': "object",
    'properties': {
        'data': {
            'type': 'array',
            'items': {
                'type': ['string', 'number', 'integer',
                         'object', 'array', 'boolean', 'null']
            },
            "minContains": 8,
            "maxContains": 8
        }
    },
    'required': ['data']
}

with open('./app/src/Models/model_test.sav', 'rb') as handle:
    pipeline = pickle.load(handle)


@Prediction_Api.route('/Single_Prediction', methods=['POST'])
def single_prediction():
    """[This api purpose is to predict a single line
    of data entered by the user through the json schema we created]
    Returns:
        [Prediction]: [it returns the model prediction of the target variable]
    """

    json: Any = pd.json_normalize(request.get_json())

    result = {
        "Prediction": pipeline.predict(json)[0],
        "status": 200
    }
    return jsonify(result)
