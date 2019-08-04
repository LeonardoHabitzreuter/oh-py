from flask import Flask, jsonify, request
from src.users.service import UsersService

app = Flask(__name__)

usersService = UsersService()

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
  if request.method == 'GET':
    return jsonify(usersService.get())
  else:
    return ''