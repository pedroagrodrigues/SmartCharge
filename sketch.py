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
from common import priceCalculation, calculateMinumumCost


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
 



def statStop():
    #addData(Base_load)
    #addData(Base_load)
    running != running
    

base_load = [1.981983333, 1.213846667, 1.011533333, 0.882773333,  0.862226667, 0.851396667, 0.850308333, 0.838041667,
6.027276667, 16.21360833,  11.764815, 20.909715, 28.57742667, 38.20092, 26.78520167, 14.98154833, 16.79817667, 8.0115,
1.292061667, 7.621555,  7.658726667,  3.668628333,  9.180846667,  2.76731]

#target = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
#target2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
# 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 
# 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 
# 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]

#

base_load_2 = [3.37647049, 14.95192063, 4.25013287, 5.30515024, 9.34320604, 0.84099285, 4.14906692, 5.92555913, 1.09218238, 
15.42361884, 2.41730785, 0.13967645, 5.20513331, 14.78998003, 5.76644157, 19.5017913, 16.91176215, 2.20395928, 8.79090141, 
11.57147527, 17.25266121, 2.8653718, 19.50209397, 13.7501223, 3.89257146, 12.1617265, 7.62182339, 5.58093061, 15.4928895, 
13.37206223, 3.05925554, 13.39755561, 18.41997117, 17.00628708, 11.02694655, 10.52463277, 13.49194292, 0.45569675, 16.95142625, 
0.7914522, 15.91105935, 5.85035416, 15.43571913, 16.20936893, 19.99708957, 13.12762015, 11.52828682, 13.48083652, 2.51020721, 
12.56000859, 6.13021093, 11.53246558, 11.7601264, 2.7965399, 14.60478201, 19.49877988, 5.1522607, 13.84780833, 2.79313481, 
10.10297839, 6.55610019, 6.03558306, 2.08877529, 8.61000145, 17.57966007, 7.15637318, 19.61904569, 15.76243068, 1.82059699, 
4.73835241, 15.02184823, 7.83263211, 19.9331165, 8.83420905, 0.396746, 8.5488508, 13.50936332, 19.91974407, 6.9081555, 10.04439587, 
17.64350539, 17.86148092, 0.18372422, 6.0196027, 9.8848701, 17.6002641, 1.45684869, 7.24992129, 6.23028015, 2.69717181, 17.00293957, 
3.43229859, 2.82024099, 18.41285865, 13.31215651, 1.22076037]

base_load_3 = [564.3, 532.8, 455.8, 643.3, 400, 383.3, 348.3, 256.2, 411.2, 245.3, 
362, 342.3, 336.8, 330.3, 251.5, 341.5, 332.5, 330.5, 250, 337.2, 327.3, 241.5, 347.3, 
333.5, 325, 242, 336.5, 329.7, 234.5, 339.7, 325.7, 319.7, 233.7, 332.8, 332.7, 238.5, 349.8, 443.3, 
412, 735, 440.8, 453, 552.5, 690.8, 663.2, 968, 491, 1022.2, 353.3, 659, 1496.8, 1045.7, 603.5, 1111.8, 
1244, 611.5, 600.5, 528.7, 460.2, 357.3, 436.2, 438, 404.5, 2644.8, 602.2, 469.7, 482.7, 563.2, 583.2, 447.7, 
582.2, 566.7, 457.8, 577.8, 567.3, 525.7, 1799.8, 1212.7, 1186.8, 686.5, 520, 509.3, 490, 1313.3, 540.8, 1594.3, 
610.3, 585, 486.7, 574.7, 610.8, 516.7, 602.2, 585, 565.7, 467.7]

base_load_4 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
10,10,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,200,200,
200,200,200,200,200,200,200,200,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,200,200,
200,200,200,200,200,200,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]

minimumCost = calculateMinumumCost(base_load_4)
print("Minimum cost for current load ", minimumCost)
popmax = 200
mutationRate = 0.1

populationInitial = Population(minimumCost, mutationRate, popmax, base_load_4)
population = Population(minimumCost, mutationRate, popmax, base_load_4)

print("Current Load: ", priceCalculation(base_load_4))


statStop()
for i in range(20):
    nextGen()

""" print(base_load_2)
print(population.getBest())
 """