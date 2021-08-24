from numpy import random
from Population import Population
    
class KnapSackSolver:

  def __init__(self):
    self.populationLength = 500
    self.population = Population()
    self.generationCount = 0
    self.itemsWeigth = [15, 3, 2, 5, 9, 20]
    self.itemsPoints = [15, 7, 10, 5, 8, 17]

  def solve(self):

    self.population.initializePopulation(self.populationLength)
    self.population.calculateFitness(self.itemsWeigth, self.itemsPoints)
    self.printGeneration()

    while self.shouldStop():

      self.crossover()

      if random.randint(0, 999)%7 < 5:
        self.mutation()
      
      self.population.calculateFitness(self.itemsWeigth, self.itemsPoints)
      self.addFittestOffspring()
      self.lastFittest = self.fittest
      self.generationCount += 1
      self.printGeneration()

  def shouldStop(self):
    if not hasattr(self, 'lastFittest'):
      return False

    count = 0
    for individual in self.population.individuals:
      if individual.fitness >= self.lastFittest.fitness:
        count += 1

    return count / self.populationLength > 0.9

  def printGeneration(self):
    self.selection()
    text = "Generation: {} Fittest score: {}"
    print(text.format(self.generationCount, self.fittest.fitness))
    print("==Genetic Pool==")
    index = 0
    for individual in self.population.individuals:
      text = "Individual {:2} => genes: {} score: {:2} weight: {:2}"
      print(text.format(index, individual.genes, individual.fitness, individual.weight))
      index += 1
    print("================\n")
    
  def selection(self):
    self.fittest = self.population.getFittest()
    self.secondFittest = self.population.getSecondFittest()

  def crossover(self):
    crossOverPoint = random.randint(0, self.population.individuals[0].geneLength)

    for i in range(0, crossOverPoint):
      temp = self.fittest.genes[i]
      self.fittest.genes[i] = self.secondFittest.genes[i]
      self.secondFittest.genes[i] = temp
  
  def mutation(self):
    mutationPoint = random.randint(0, self.population.individuals[0].geneLength)

    self.fittest.genes[mutationPoint] = not self.fittest.genes[mutationPoint]

    mutationPoint = random.randint(0, self.population.individuals[0].geneLength)

    self.secondFittest.genes[mutationPoint] = not self.secondFittest.genes[mutationPoint]

  def addFittestOffspring(self):
    self.fittest.calculateFitness(self.itemsWeigth, self.itemsPoints)
    self.secondFittest.calculateFitness(self.itemsWeigth, self.itemsPoints)
    leastFittest = self.population.getLeastFittest()
    self.population.individuals[self.population.individuals.index(leastFittest)] = self.getFittestOffspring()

  def getFittestOffspring(self):
    return self.fittest if self.fittest.fitness > self.secondFittest.fitness else self.secondFittest