from common import getData
from math import ceil
from Facade import Facade


endDate = '2018-08-31T23:59:59.999Z'

for i in range(1, 6):
    plug = str(i)
    day = 1
    initialDate = ''
    data = []
    
    while initialDate.split('T')[0] != endDate.split('T')[0]:
        initialDate = f'2018-08-{day:02d}T00:00:00.000Z'
        finalDate = f'2018-08-{day:02d}T23:59:59.999Z'
        newData = getData(plug,initialDate, finalDate, False)
        if (sum(newData)!=0):
            data.append(newData)
        day += 1

    initialCost = 0
    calculatedCost = 0
    for j in range(len(data)):
        data[j] = Facade(data[j])
        initialCost += data[j].inputPrice
        for _ in range(50):
            data[j].nextGen()
        calculatedCost += data[j].getCost()
    print (f'For the plug {plug}:')
    print(f'The initial cost was: {initialCost}€')
    print(f'The cost calculated was: {calculatedCost}€')


