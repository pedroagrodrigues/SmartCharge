# The Nature of Code
# Daniel Shiffman
# http:#natureofcode.com

# Genetic Algorithm, Evolving Shakespeare

# Demonstration of using a genetic algorithm to perform a search

# setup()
#  # Step 1: The Population
#    # Create an empty population (an array or ArrayList)
#    # Fill it with DNA encoded objects (pick random values to start)

# draw()
#  # Step 1: Selection
#    # Create an empty mating pool (an empty ArrayList)
#    # For every member of the population, evaluate its fitness based on some criteria / function,
#      and add it to the mating pool in a manner consistant with its fitness, i.e. the more fit it
#      is the more times it appears in the mating pool, in order to be more likely picked for reproduction.

#  # Step 2: Reproduction Create a new empty population
#    # Fill the new population by executing the following steps:
#       1. Pick two "parent" objects from the mating pool.
#       2. Crossover -- create a "child" object by mating these two parents.
#       3. Mutation -- mutate the child's DNA based on a given probability.
#       4. Add the child object to the new population.
#    # Replace the old population with the new population
#
#   # Rinse and repeat
from Population import Population
from math import floor

cost_n = 0.14
cost_v = 0.12
cost_p = 0.20

running = False


#def setup():
# bestPhrase = createP("Best Fit:")
# #bestPhrase.position(10,10)
# bestPhrase.class("best")

# allPhrases = createP("All phrases:")
# allPhrases.position(600, 10)
# allPhrases.class("all")

# stats = createP("Stats")
# #stats.position(10,200)
# stats.class("stats")




def nextGen():
    #if running:
    # Generate mating pool
    population.naturalSelection()
    #Create next generation
    population.generate()
    # Calculate fitness
    population.calcFitness()
    population.evaluate()
    # If we found the target phrase, stop
    #if population.isFinished():
        #println(millis()/1000.0)
    #     noLoop()
    # subsData(population.getBest())
    #displayInfo()
    #delay(100)

     
# def displayInfo():
#     # Display current status of population
#     answer = population.getBest()

#     bestPhrase.html("Best Load fit:<br>" + answer)
#     statstext = "total generations:     " + population.getGenerations() + "<br>"
#     statstext += "average fitness:       " + population.getAverageFitness() + "<br>"
#     statstext += "total population:      " + popmax + "<br>"
#     statstext += "mutation rate:         " + floor(mutationRate * 100) + "%"

#     stats.html(statstext)

#     allPhrases.html("All possible loads:<br>" + population.allPhrases()) 
    

# the minimum consumption is  equal to all consumption happening in vazio
 

def calculateMinumumCost(load):
    total = 0
    for i in range(len(load)):
        total += load[i]*cost_v
    return total

def statStop():
    #addData(Base_load)
    #addData(Base_load)
    running != running
    

base_load = [1.981983333, 1.213846667, 1.011533333, 0.882773333,  0.862226667, 0.851396667, 0.850308333, 0.838041667,
6.027276667, 16.21360833,  11.764815, 20.909715, 28.57742667, 38.20092, 26.78520167, 14.98154833, 16.79817667, 8.0115,
1.292061667, 7.621555,  7.658726667,  3.668628333,  9.180846667,  2.76731]

#target = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

minimumCost = calculateMinumumCost(base_load)
print("Minimum cost for current load ", minimumCost)
popmax = 500
mutationRate = 0.01

population = Population(minimumCost, mutationRate, popmax, base_load)

print("Current Load: ", population.calculateCost(base_load))

statStop()
for i in range(20):
    nextGen()

print(base_load)
print(population.getBest())
