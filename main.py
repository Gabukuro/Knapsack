from KnapSack import KnapSackSolver

populationLength = 500
itemsWeigth = [15, 3, 2, 5, 9, 20]
itemsPoints = [15, 7, 10, 5, 8, 17]
maxWeight = 30

knapSackSolver = KnapSackSolver(itemsWeigth, itemsPoints, maxWeight, populationLength)
knapSackSolver.solve()