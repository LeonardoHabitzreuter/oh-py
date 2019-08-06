# -*- coding: utf-8 -*-
from playhouse.shortcuts import model_to_dict
from ..database.models import User

class UsersService:
  def get(self):
    return list(map(model_to_dict, User.select()))

  def create(self, request):
    User.create(name=request.get("name"), age=request.get("age"))
    User(name=request.get("name"), age=request.get("age")).save()
    return 'created'

  def delete(self, id):
    deleted = User.delete().where(User.id == id).execute()
    return "deleted" if deleted > 0 else "id not found", 404