from src.database.models import connect, createTables
from src.services.userService import UsersService
from src.services.productsService import ProductsService
from src.services.ordersService import OrdersService

createTables()
connect()

usersService = UsersService()
productsService = ProductsService()
ordersService = OrdersService()

def test():
  user = usersService.create({ 'name': 'userTest', 'age': 0 }).data
  product = productsService.create({ 'name': 'productTest', 'price': 1.1 }).data
  ordersService.create({ 'productId': product, 'userId': user })
  orders = ordersService.get().data
  print(orders)

test()