
# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# A class to describe a pseudo-DNA, i.e. genotype
#   Here, a virtual organism's DNA is an array of character.
#   Functionality:
#      -- convert DNA into a string
#      -- calculate DNA's "fitness"
#      -- mate DNA with another set of DNA
#      -- mutate DNA

from math import floor
from random import random, randrange
from common import priceCalculation, createRandomSchedule

class DNA:
    #the DNA receives the load of the house, and what will change is the arrangement of the consumption
    def __init__(self, num, load):
        self.genes = createRandomSchedule(num)
        self.load = self.assignLoad(load, num)
        self.fitness = 0


    def assignLoad(self, load, num):
        temp = []
        for i in range(num):
            temp.append(load[self.genes[i]])
        return temp

    def calcFitness(self, target):
        total_cost = priceCalculation(self.load)
        total_score = target / total_cost
        self.fitness = total_score
  

    def checkScheduleAvail(self, schedule, time):
        result = True
        for i in range(len(schedule)):
            if schedule[i] == time:
                result = False
        return result
  

    def insertNextElem(self, currentSchedule):
        result = 0
        solution = False
        for i in range(93):
            for j in range(len(currentSchedule)):
                if(currentSchedule[j]==i):
                    solution = False
                    break
                else:
                    solution = True
            if solution:
                result = i
                break
        return result
  

    def crossoverNew(self, partner):
        #A new child
        child = DNA(len(self.load), self.load)
        for i in range(len(child.genes)):
            child.genes[i] = -1
        #midpoint = floor(random(len(self.genes))) #Pick a midpoint
        midpoint = floor(len(self.genes)/2) #Pick a midpoint
        #Half from one, half from the other
        for i in range(len(self.genes)):
            if i > midpoint:
                if self.checkScheduleAvail(child.genes, self.genes[i]):
                    child.genes[i] = self.genes[i]
                else:
                    #print('prob aqui ', self.genes[i])
                    child.genes[i] = self.insertNextElem(child.genes)
        
            else:
                if (self.checkScheduleAvail(child.genes, partner.genes[i])):
                    child.genes[i] = partner.genes[i]
                else: 
                    #print ('prob aqui '+partner.genes[i])
                    child.genes[i] = self.insertNextElem(child.genes)
     
        return child
  

    #Crossover
    def crossover(self, partner):
        return self.crossoverNew(partner)
    

    #Based on a mutation probability, picks a new random character
    def mutate(self, mutationRate):
        #randomSchedule = createRandomSchedule()
        for i in range(len(self.genes)):
            if random() < mutationRate:
                index = floor(randrange(23))
                temp = self.genes[i]
                self.genes[i] = self.genes[index]
                self.genes[index] = temp

