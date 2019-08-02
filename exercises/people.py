# -*- coding: utf-8 -*-

class Listing:
  people = ['João de Oliveira', 'Maria da Silva', 'Teresa Mattos', 'Paulo José Có', 'Jorge Lacerda', 'Maria Rick Jou']

  def question1(self, search):
    for i, person in enumerate(self.people):
      if search in person:
        print(person + ' ' + str(i))
        # print(' '.join([person, str(i)]))

  def question1B(self):
    peopleDictionary = {}
    # sample = dict([(<key>, <value>), (<key>, <value)])
    for person in self.people:
      for word in person.split():
        current = peopleDictionary.get(word, 0)
        peopleDictionary[word] = current + 1

    print(peopleDictionary)


myClass = Listing()

myClass.question1B()