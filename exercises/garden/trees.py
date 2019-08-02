from garden import Garden

garden = Garden()

garden.trees.append({
  'especie': 'bananeira', 'limite': 20,
  'fator': 1.11, 'alturas': [4],
})
garden.trees.append({
  'especie': 'laranjeira', 'limite': 15,
  'fator': 1.1,
  'alturas': [3]
})

garden.grow()
garden.show()