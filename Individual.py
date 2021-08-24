from numpy import random

class Individual:

  def __init__(self):
    self.weight = 0
    self.fitness = 0
    self.geneLength = 6
    self.genes = random.randint(2, size=self.geneLength)

  def calculateFitness(self, itemsWeigth, itemsPoints):
    self.fitness = 0
    self.weight = 0
    maxWeight = 30
    for i in range(self.geneLength):
      if self.genes[i] == 1 and self.weight + itemsWeigth[i] <= maxWeight:
        self.fitness += itemsPoints[i]
        self.weight += itemsWeigth[i]