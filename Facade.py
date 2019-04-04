from Population import Population
from math import floor
import numpy
from matplotlib import pyplot
from common import priceCalculation, calculateMinumumCost, fileReader, getData

class Facade:
    def __init__(self, baseLoad):
        self.baseLoad = baseLoad
        self.minimumCost = calculateMinumumCost(self.baseLoad)
        self.mutationRate = 0.1 #<----------------------------------This variable is suppose to be loaded from config file
        self.maxPopulation = 10 #<----------------------------------This variable is suppose to be loaded from config file
        self.inputPrice = priceCalculation(baseLoad) #calculates the price for the inputed load
        fileReader()
        self.graph_pyplotInitializer()
        self.population = self.createPopulation(self.minimumCost, self.mutationRate, self.maxPopulation, self.baseLoad)


    def graph_pyplotInitializer(self):
        x = numpy.linspace(0, len(self.baseLoad), len(self.baseLoad)) #x axis
        pyplot.xlabel('Tempo')
        pyplot.ylabel('Carga')
        pyplot.title('SmartCharge')
        pyplot.plot(x, self.baseLoad, label='Baseload')

    
    def nextGen(self):
        self.population.naturalSelection()
        self.population.generate()
        self.population.calcFitness()
        self.population.evaluate()

    def createPopulation(self, minimumCost, mutationRate, maxPopulation, baseload):
        return Population(minimumCost, mutationRate, maxPopulation, baseload)


