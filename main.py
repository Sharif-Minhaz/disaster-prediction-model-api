from flask import Flask, jsonify, request

from utils.predict_disaster import predict_disaster

app = Flask(__name__)


@app.route("/")
def test():
    text = "Model is running perfectly"
    responseData = {
        "status": 200,
        "success": True,
        "message": text,
    }

    return jsonify(responseData)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        request_data = request.json  # Parse JSON data from request body

        # Check if 'date' and 'location' keys are in the JSON data
        if 'date' in request_data and 'location' in request_data:
            date = request_data['date']
            location = request_data['location']

            # Call predict_disaster function with date and location
            res = predict_disaster(date, location)

            responseData = {
                "status": 200,
                "success": True,
                "data": res,
            }
        else:
            responseData = {
                "status": 400,
                "success": False,
                "message": "Missing 'date' or 'location' in JSON data",
            }
    else:
        responseData = {
            "status": 400,
            "success": False,
            "message": "Invalid request method",
        }

    return jsonify(responseData)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True, host="0.0.0.0", port=5001)
