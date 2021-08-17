from numpy import random

class Population:

  def __init__(self):
    self.popSize = 10
    self.individuals = []
    self.fittest = 0

  def initializePopulation(self, size):
    self.popSize = size
    for i in range(self.popSize):
      self.individuals.append(Individual())


class Individual:

  def __init__(self):
    self.fitness = 0
    self.geneLength = 6
    self.genes = random.randint(2, size=self.geneLength)

  def calculateFitness(self):
    self.fitness = 0
    for i in self.genes:
      if i == 1:
        ++self.fitness


population = Population()
population.initializePopulation(10)

for val in population.individuals:
  print(val.genes)

# items = [15, 3, 2, 5, 9, 20]
# value = [15, 7, 10, 5, 8, 17]