from playhouse.shortcuts import model_to_dict
from src.database.models import User
from .response import Response

class UsersService:
  def get(self):
    users = list(map(model_to_dict, User.select()))
    return Response(data=users)

  def create(self, request):
    user = User.create(name=request.get("name"), age=request.get("age"))
    return Response(data=user)

  def delete(self, id):
    deleted = User.delete().where(User.id == id).execute()
    return Response() if deleted > 0 else Response(data="id not found", status=404)
  
  def update(self, id, user):
    query = User.update(user).where(User.id == id)
    updated = query.execute()
    return Response() if updated > 0 else Response(data="id not found", status=404)