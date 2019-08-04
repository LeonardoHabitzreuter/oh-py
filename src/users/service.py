# -*- coding: utf-8 -*-

class UsersService:
  def get(self):
    return [{ 'name': 'Jhon', 'age': 25 }, { 'name': 'Mary', 'age': 23 }]

  def create(self, request):
    return { 'name': request.get("name"), 'age': request.get("age") }