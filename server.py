from flask import Flask, request
from src.services.userService import UsersService
from src.services.productsService import ProductsService
from src.services.ordersService import OrdersService
from src.database.models import connect, createTables

app = Flask(__name__)

usersService = UsersService()
productsService = ProductsService()
ordersService = OrdersService()
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

@app.route('/products', methods=['GET', 'POST'])
def products():
  return productsService.get().toJson() if request.method == 'GET' else productsService.create(request.get_json()).toJson()

@app.route('/products/<int:id>', methods=['PUT'])
def updateProduct(id):
  return productsService.update(id, request.get_json()).toJson()

@app.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
  return productsService.delete(id).toJson()

@app.route('/orders', methods=['GET', 'POST'])
def orders():
  return ordersService.get().toJson() if request.method == 'GET' else ordersService.create(request.get_json()).toJson()