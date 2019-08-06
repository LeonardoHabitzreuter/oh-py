from flask import Flask, jsonify, request
from src.users.service import UsersService
from src.database.models import connect, createTables

app = Flask(__name__)

usersService = UsersService()
createTables()

@app.before_request
def before_request():
  print('here')
  connect()

@app.route('/users', methods=['GET', 'POST', 'PUT'])
def users():
  if request.method == 'GET':
    return jsonify(usersService.get())
  if request.method == 'POST':
    return jsonify(usersService.create(request.get_json()))
  else:
    return ''

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
  return usersService.delete(userId)