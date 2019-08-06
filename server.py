from flask import Flask, request
from src.services.userService import UsersService
from src.database.models import connect, createTables

app = Flask(__name__)

usersService = UsersService()
createTables()

@app.before_request
def before_request():
  connect()

@app.route('/users', methods=['GET', 'POST', 'PUT'])
def users():
  if request.method == 'GET':
    return usersService.get().toJson()
  if request.method == 'POST':
    return usersService.create(request.get_json()).toJson()
  else:
    return ''

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
  return usersService.delete(userId).toJson()