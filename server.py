from flask import Flask, request
from src.services.userService import UsersService
from src.database.models import connect, createTables

app = Flask(__name__)

usersService = UsersService()
createTables()

@app.before_request
def before_request():
  connect()

@app.route('/users', methods=['GET', 'POST'])
def users():
  return usersService.get().toJson() if request.method == 'GET' else usersService.create(request.get_json()).toJson()

@app.route('/users/<int:userId>', methods=['PUT'])
def updateUser(userId):
  return usersService.update(userId, request.get_json()).toJson()

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
  return usersService.delete(userId).toJson()