from flask import Flask, jsonify
import camelcase

app = Flask(__name__)

@app.route("/")
def hello_world():
    cr7 = camelcase.CamelCase()  # cr7 === camel ∞
    idolsCommitment = cr7.hump("data segmentation map")
    
    responseData = {
        "success": True,
        "message": idolsCommitment,
    }
    
    return jsonify(responseData)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
