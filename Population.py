# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# A class to describe a population of virtual organisms
# In this case, each organism is just an instance of a DNA object
'''
     NUMA PRIMEIRA ABORDAGEM VAMOS APENAS USAR UMA LOAD BASE E TENTAR REARRANJAR OS CONSUMOS DE FORMA A DMINIUIR
    O CUSTO TOTAL BASEADO EM 3 TARIFAS

    VAMOS TENTAR MINIMIZAR ATE AO VALOR IMPOSSÍVEL EM QUE TODO O CONSUMO ACONTECE NO VAZIO
'''
from DNA import DNA
from math import floor
from random import random, randrange

class Population:
    def __init__(self, target, mutationRate, num, firstLoad):
        self.population = [] #Array to hold the current population
        self.matingPool = [] #ArrayList which will be used for the "mating pool"
        self.generations = 0 #Number of generations
        self.finished = False #Is the evolution over?
        self.target = target #Target which we are hoping to achieve
        self.mutationRate = mutationRate #Mutation rate
        self.perfectScore = 0.8
        self.original_load = firstLoad
        self.best = ""
        
        self.population = [] 
        for i in range(num):
            self.population.append(DNA(len(firstLoad), firstLoad))

        self.calcFitness()

    #Não faz muito sentido -- Recursiva sem paragem? 
    def calcFitness(self):
        for i in range(len(self.population)):
            self.population[i].calcFitness(self.target)

    def calculateCost(self, load):
        cost_n = 0.14
        cost_v = 0.12
        cost_p = 0.20
        total_cost = 0
        for i in range(len(load)):
            if (i < len(load)*6/24):
                total_cost += load[i] * cost_v
            elif (i < 12*len(load)/24):
                total_cost += load[i] * cost_n
            elif (i < 14*len(load)/24):
                total_cost += load[i] * cost_p
            elif (i < 18*len(load)/24):
                total_cost += load[i] * cost_n
            elif (i < 20*len(load)/24):
                total_cost += load[i] * cost_p
            elif (i <= 23*len(load)/24):
                total_cost += load[i] * cost_n
        return total_cost
  
    #Generate a mating pool
    def naturalSelection(self):
        #Clear the ArrayList
        #print("Tamanho ", len(self.population[0].genes))
        self.matingPool = []
        maxFitness = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > maxFitness:
                maxFitness = self.population[i].fitness

        #Based on fitness, each member will get added to the mating pool a certain number of times
        #a higher fitness = more entries to mating pool = more likely to be picked as a parent
        #a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
   
        for i in range(len(self.population)):
            fitness = self.normalize(self.population[i].fitness, maxFitness)
            n = floor(fitness * 100) #Arbitrary multiplier, we can also use monte carlo method
            for j in range(n):  #and pick two random numbers
                self.matingPool.append(self.population[j])
      
    
    
    def normalize(self, currentPopulation, maxFitness):
       return currentPopulation/maxFitness


    #Create a new generation
    def generate(self):
        #Refill the population with children from the mating pool
        for i in range(len(self.population)):
            a = randrange(len(self.matingPool))
            b = randrange(len(self.matingPool))
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            self.population[i] = child
        
        self.generations += 1 
    
    def getBest(self):
        best_load = []
        #print ("best é: ", self.best)
        for i in range(len(self.original_load)):
            best_load.append(self.original_load[self.best[i]])
            #print(self.best[i]);
        return best_load
  
    #Compute the current "most fit" member of the population
    def evaluate(self):
        worldrecord = 0.0
        index = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > worldrecord:
                index = i
                worldrecord = self.population[i].fitness
            #print(str(self.population[i]))
        self.best = self.population[index].getPhrase()

        print("World reccord: ", worldrecord)
        """ for i in range(len(self.best)):
            print(str(self.original_load[self.best[i]])) """
        if worldrecord > self.perfectScore:
            self.finished = True
    
    def isFinished(self):
        return self.finished
    
    def getGenerations(self):
        return self.generations

    #Compute average fitness for the population
    def getAverageFitness(self):
        total = 0
        for i in range(len(self.population)):
            total += self.population[i].fitness
        try:    
            return total / len(self.population)
        except:
            return 0