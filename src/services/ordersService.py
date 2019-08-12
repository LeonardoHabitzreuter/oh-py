from playhouse.shortcuts import model_to_dict
from src.database.models import Product, User, Order
from .response import Response

class OrdersService:
  def get(self):
    orders = list(map(model_to_dict, Order.select()))
    return Response(data=orders)

  def create(self, order):
    user = User.get_or_none(User.id == order.get("userId"))
    if user == None:
      return Response(data="userId not found", status=404)

    product = Product.get_or_none(Product.id == order.get("productId"))
    if product == None:
      return Response(data="productId not found", status=404)

    Order.create(product=product, user=user)
    return Response()