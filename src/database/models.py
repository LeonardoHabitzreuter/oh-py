import sqlite3
from peewee import *

db = SqliteDatabase('people.db')

class BaseModel(Model):
  class Meta:
    database = db

class User(BaseModel):
  name = CharField()
  age = IntegerField()

class Product(BaseModel):
  name = CharField()
  price = FloatField()

class Order(BaseModel):
  user = ForeignKeyField(User, backref='orders')
  product = ForeignKeyField(Product, backref='orders')

def connect():
  db.connect()

def createTables():
  with db:
    db.create_tables([User, Product, Order])