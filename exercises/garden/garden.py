# -*- coding: utf-8 -*-

class Garden:
  def __init__(self):
    self.trees = []

  def grow(self):
    toContinue = True
    while toContinue:
      for tree in self.trees:
        # takeLast
        height = tree['alturas'][-1]
        newHeight = height + tree['fator']
        tree['alturas'].append(newHeight)
        if newHeight > tree['limite']:
          toContinue = False
        # zfill fixa 5 caracters, eg 4 -> 00004
        tmp = format(height, ".2f").zfill(5)
        print(tmp, ">", tree['limite'], "? | ", end="")
      # pula linha
      print()
    print("Final heights reached")

  def show(self):
    for tree in self.trees:
      height = tree['alturas'][-1]
      # 2f = arredonda 2 casas decimais
      print(tree['especie'], ":", "{0:.2f}".format(height))
