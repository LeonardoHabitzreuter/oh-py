# -*- coding: utf-8 -*-

from mobilia import Table, Chair, FeetChair, WheelChair, MagneticChair

m = Table()
m.chairs.append(FeetChair())
m.chairs.append(WheelChair(material="Plástico"))
m.chairs.append(MagneticChair(baseWeight=2, material="Plástico"))
print("Mesa com",m.lugares,"lugares")
for chair in m.chairs:
  print(chair)
