from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "data": data,
        "message": "success"
    }),200

@app.route("/planet")

def planet():

    name = request.args.get("name")
    
    #next = find data inside dictionary
    planet_data = next(item for item in data if item["name"] == name)

    return jsonify({
        "data" : planet_data,
        "message" : "success"
    }),200

if __name__ == "__main__":
    app.run(debug = True)

