from playhouse.shortcuts import model_to_dict
from src.database.models import Product
from .response import Response

class ProductsService:
  def get(self):
    products = list(map(model_to_dict, Product.select()))
    return Response(data=products)

  def create(self, request):
    product = Product.create(name=request.get("name"), price=request.get("price"))
    return Response(data=product)

  def delete(self, id):
    deleted = Product.delete().where(Product.id == id).execute()
    return Response() if deleted > 0 else Response(data="id not found", status=404)
  
  def update(self, id, product):
    query = Product.update(product).where(Product.id == id)
    updated = query.execute()
    return Response() if updated > 0 else Response(data="id not found", status=404)