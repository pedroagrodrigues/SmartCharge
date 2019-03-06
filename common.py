#   This file has all the functions that may be used for more than one class.



#   Default variables

cost_n = 0.14
cost_v = 0.12
cost_p = 0.20


#   Initializer to the variables, if you don't want to use default values, you call this function
#and provide the new valies. 

def varInitializer(value_n, value_v, value_p, valueTotalCost):
    cost_n = value_n
    cost_v = value_v
    cost_p = value_p
    totalCost = valueTotalCost


#   This function is able to calculate how much you will pay for a given individual
def priceCalculation(individual):
    day = len(individual) / 24 #This will scale any given population to 24 hours
    totalCost = 0
    for i in range(len(individual)):
        if i < 6 * day:
            totalCost += individual[i] * cost_v
        elif i < 12 * day:
            totalCost += individual[i] * cost_n
        elif i < 14 * day:
            totalCost += individual[i] * cost_p
        elif i < 18 * day:
            totalCost += individual[i] * cost_n
        elif i < 20 * day:
            totalCost += individual[i] * cost_p
        elif i <= 23 * day:
            totalCost += individual[i] * cost_n
    
    return totalCost

#   Carefull, to use this function the hour must be converted to 24 formula: X = len(Array) / 24
#   Work in progress --- Need to understand, comes from DNA class calculateSingleCost
def priceSingleCost(value, hour):
    totalCost = 0
    if hour < 6:
        totalCost = value * cost_v
    elif hour < 12:
        totalCost = value * cost_n
    elif hour < 14:
        totalCost = value * cost_p
    elif hour < 18:
        totalCost = value * cost_n
    elif hour < 20:
        totalCost = value * cost_p
    elif hour <= 23:
        totalCost = value * cost_n
    return totalCost
