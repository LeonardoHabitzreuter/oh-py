# -*- coding: utf-8 -*-

class Chair:
  def __init__(self, material="Madeira"):
    self.material = material

class WheelChair(Chair):
  def __init__(self, wheelCount=0, wheelType='', **kwargs):
    super().__init__(**kwargs)
    self.wheelCount = 8
    self.wheelType = "Metal" #poliuretano,polipropileno,etc

  def __str__(self):
    return "Cadeira de "+self.material+" com "\
    + str(self.wheelCount)+" rodas de "+self.wheelType
  
class FeetChair(Chair):
  def __init__(self, feetCount=0, **kwargs):
    super().__init__(**kwargs)
    self.feetCount = 4
  
  def __str__(self):
    return "Cadeira de "+self.material+" com " + str(self.feetCount)+" pés"

class MagneticChair(Chair):
  def __init__(self, baseWeight=1, **kwargs):
    super().__init__(**kwargs)
    self.baseWeight = baseWeight
  
  def __str__(self):
    return "Cadeira de "+self.material+" com base magnética de " + str(self.baseWeight)+"kg"

class Table:
  def __init__(self):
    self.lugares = 4
    self.chairs = []