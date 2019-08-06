import sqlite3
from peewee import *

db = SqliteDatabase('people.db')

class User(Model):
  name = CharField()
  age = IntegerField()

  class Meta:
    database = db

  def __str__(self):
    return self.name

def connect():
  db.connect()

def createTables():
  with db:
    db.create_tables([User])