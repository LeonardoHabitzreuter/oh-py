from flask import jsonify

class Response:
  def __init__(self, data="Ok", status=200):
    self.data = data
    self.status = status

  def toJson(self):
    return jsonify(self.data), self.status