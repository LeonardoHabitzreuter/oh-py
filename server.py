from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def hello():
  return jsonify([{ 'name': 'Jhon', 'age': 25 }, { 'name': 'Mary', 'age': 23 }])