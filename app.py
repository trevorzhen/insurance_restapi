from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from joblib import load
import numpy as np

APP = Flask(__name__)
API = Api(APP)

insurance_model = load('insurance.mdl')

class Predict(Resource):

    @staticmethod
    def post():
        # args = request.json

        instance = reqparse.RequestParser()
        instance.add_argument('Age')
        instance.add_argument('BMI')
        instance.add_argument('Sex')
        instance.add_argument('Children') # Number of Children (0-5)
        instance.add_argument('Smoker')   # Yes = 1 or No = 0
        instance.add_argument('Region')   # Options: 1,2,3 or 4
        args = instance.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        vec_children = np.zeros(5)
        vec_region = np.zeros(3)
        if X_new[3] > 0:
            vec_children[int(X_new[3])-1] = 1
        if X_new[-1] > 1:
            vec_region[int(X_new[-1])-2] = 1
        X_new = np.delete(X_new, 3)
        X_new = np.insert(X_new, 3,  vec_children)
        X_new = np.insert(X_new, -1, vec_region)
        X_new = np.delete(X_new, -1)
        
        out = {'Prediction': round(insurance_model.predict([X_new])[0],2), 'X_new':args}

        return out, 200

API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True, port='1080')