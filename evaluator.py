from common import getData
from math import ceil
from Facade import Facade


endDate = '2018-08-31T23:59:59.999Z'
averageInput = []
averageOutput = []
for _ in range(96):
    averageInput.append(0)
    averageOutput.append(0)
     
for i in range(1, 6):
    plug = str(i)
    day = 1
    initialDate = ''
    data = []
    
    while initialDate.split('T')[0] != endDate.split('T')[0]:
        initialDate = f'2018-08-{day:02d}T00:00:00.000Z'
        finalDate = f'2018-08-{day:02d}T23:59:59.999Z'
        newData = getData(plug, initialDate, finalDate, 'false')
        if (sum(newData) != 0):
            data.append(newData)
        day += 1
    print('data has ', day, 'days')

    initialCost = 0
    calculatedCost = 0
    for j in range(len(data)):
        for k in range(len(data[j])):
            averageInput[k] += data[j][k] 
            print ('adding inputs')
        data[j] = Facade(data[j])
        initialCost += data[j].inputPrice
        for _ in range(50):
            data[j].nextGen()
        calculatedCost += data[j].getCost()
        for k in range(len(data[j].population.bestRecord[1])):
            averageOutput[k] += data[j].population.bestRecord[1][k]
            print('running k: ', k)
    print(f'For the plug {plug}:')
    print(f'The initial cost was: {initialCost}€')
    print(f'The cost calculated was: {calculatedCost}€\n')

    
    for p in range(96):
        averageInput[p] /= 31
        averageOutput[p] /= 31
        

    f = open('teste.txt', 'a')
    f.writelines(f'For plug {plug}:\n')
    f.write(f'Input: {averageInput}\n')
    f.write(f'Output: {averageOutput}\n')
    f.close()
    print(f'For plug {plug}:\n')
    print(f'Input: {averageInput}\n')
    print(f'Output: {averageOutput}\n')
    


