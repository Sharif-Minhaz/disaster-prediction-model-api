from flask import Flask, jsonify

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

@app.route("/predict")
def predict():
    responseData = {
        "status": 200,
        "success": True,
        "message": "Prediction result: 'Here'",
    }
    
    return jsonify(responseData)


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True, host="0.0.0.0", port=5001)
