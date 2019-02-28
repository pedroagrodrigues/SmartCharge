
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

class DNA:
    #the DNA receives the load of the house, and what will change is the arrangement of the consumption
    def __init__(self, num, load):
        self.load = load
        self.fitness = 0
        self.genes = createRandomSchedule(load)

    '''
        Alterar aqui
    '''
    def calculateCost(self, load):
        cost_n = 0.14
        cost_v = 0.12
        cost_p = 1 #0.20
        total_cost = 0
        
        for i in range(len(load)):
            if i < 6 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_v
            elif i < 12 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_n
            elif i < 14 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_p
            elif i < 18 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_n
            elif i < 20 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_p
            elif i <= 23 * len(load) / 24:
                total_cost += self.load[load[i]] * cost_n

        return total_cost


    def calculateSingleCost(self, value, hour):
        cost_n = 0.14
        cost_v = 0.12
        cost_p = 1 #0.2
        total_cost = 0
        if hour < 6*4:
            total_cost = value * cost_v
        elif hour < 12*4:
            total_cost = value * cost_n
        elif hour < 14*4:
            total_cost = value * cost_p
        elif hour < 18*4:
            total_cost = value * cost_n
        elif hour < 20*4:
            total_cost = value * cost_p
        elif hour <= 23*4:
            total_cost = value * cost_n
        return total_cost
  

    def calcFitness(self, target):
        total_cost = self.calculateCost(self.genes)
        total_score = target / total_cost
        self.fitness = total_score
        #print("totalCost: ", total_cost, " totalScore: ", total_score)
        #self.fitness = self.fitness ** 2
  

    #Fitness function (returns floating point % of "correct" characters)
    def calcFitness2(self, target):
        score = 0
        scores = []
        
        for i in range(len(self.genes)):
            score = abs(self.genes[i] / target[i])
            score = 1 - (score - 1) if score > 1 else score
            score = 220*16 - score
            #score = 1 -(score / (220*16))
            scores[i] = score

            total_score = 0
        
        for i in range(len(scores)):
            total_score += scores[i]
        self.fitness = total_score/len(scores)
        
    
    def checkScheduleComplete(self, schedule):
        result = True
        for i in range(len(schedule)):
            if schedule[i] == -1:
                result = False
        return result

    def checkScheduleAvail(self, schedule, time):
        result = True
        for i in range(len(schedule)):
            if schedule[i] == time:
                result = False
        return result
  
    def getPhrase(self):
        return self.genes


    def crossoverSchedule(self, partner):
        child = DNA(len(self.load), self.load)
        for i in range(len(child.genes)):
            child.genes[i] = -1

        self.crossoverNew(partner)

        for i in range(len(child.genes)):
            if self.calculateSingleCost(self.load[self.genes[i]], i*(len(self.load)/24)) < self.calculateSingleCost(self.load[partner.genes[i]], i*(len(self.load)/24)):
                if child.genes[i] == -1:
                    if self.checkScheduleAvail(child.genes, self.genes[i]):
                        child.genes[i] = self.genes[i]
                    else:
                        child.genes[i] = -2
            if child.genes[i] == -2:
                pass
                #print ('repetido')
            else:
                if child.genes[i] == -1:
                    if self.checkScheduleAvail(child.genes, partner.genes[i]):
                        child.genes[i] = partner.genes[i]
                    else:
                        child.genes[i] = -2
        return child
  

    def checkRepetitions(self, child):
        #repetition = False
        #print ("tamanho child ", len(child))
        for i in range(len(child)):
            for j in range(len(child)):
                if child[i] == child[j] and i != j:
                    #print (str(child[i]), " ---> REPETITION")
                    return
        #print("NO REPETITION")
  
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
        
      
    
        #print("--->", this.genes);
        #print("--->", partner.genes);
        #print("--->", child.genes);
        #self.checkRepetitions(child.genes)
        return child
  
    #Crossover
    def crossover(self, partner):
        #A new child
        #child = DNA(24, self.load);
        #midpoint = floor(random(floor(len(child.genes)))) #Pick a midpoint
        #midpoint = floor(len(child.genes)/2) #Pick a midpoint
        # # Half from one, half from the other

        #for i in range(len(self.genes)):
        #     if i > midpoint:
        #         child.genes[i] = self.genes[i]
        #   else:
        #       child.genes[i] = partner.genes[i]
    
        #return child
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


def createRandomSchedule(load):
    day = []

    for i in range(len(load)):
        day.append(i)

    ctr = len(day)

    #While there are elements in the array
    while ctr > 0:
        #Pick a random index
        index = floor(random() * ctr)
        #Decrease ctr by 1
        ctr -= 1
        #And swap the last element with it
        temp = day[ctr]
        day[ctr] = day[index]
        day[index] = temp
    return day
