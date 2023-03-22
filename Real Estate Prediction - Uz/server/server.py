from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'district': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():

    rooms = int(request.form['rooms'])
    size = float(request.form['size'])
    level = int(request.form['level'])
    district = request.form['district']

    response = jsonify({
        'estimated_price': util.predict_home_price(rooms, size, level, district)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artefacts()
    app.run()