from Individual import Individual

class Population:

  def __init__(self):
    self.popSize = 10
    self.individuals = []
    self.fittest = 0

  def initializePopulation(self, size):
    self.popSize = size
    for i in range(self.popSize):
      self.individuals.append(Individual())
    
  def calculateFitness(self, itemsWeigth, itemsPoints, maxWeight):
    for individual in self.individuals:
      individual.calculateFitness(itemsWeigth, itemsPoints, maxWeight)
  
    self.getFittest()
  
  def getFittest(self):
    maxFit = 0
    for individual in self.individuals:
      if maxFit <= individual.fitness:
        maxFit = individual.fitness
        maxFitIndividual = individual

    self.fittest = maxFitIndividual.fitness 
    return maxFitIndividual

  def getSecondFittest(self):
    maxFit2 = self.fittest
    for individual in self.individuals:
      if self.fittest >= individual.fitness and maxFit2 <= individual.fitness:
        maxFit2 = individual.fitness
        secondFitIndividual = individual

    return secondFitIndividual

  def getLeastFittest(self):
    minFit = self.fittest
    for individual in self.individuals:
      if individual.fitness <= minFit:
        minFit = individual.fitness
        leastFittest = individual

    return leastFittest