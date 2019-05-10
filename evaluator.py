from common import getData
from math import ceil
from Facade import Facade

#2885

plug = '6'
day = 1
initialDate = ''
endDate = '2018-08-31T23:59:59.999Z'

data = []

while initialDate.split('T')[0] != endDate.split('T')[0]:
    initialDate = f'2018-08-{day:02d}T00:00:00.000Z'
    finalDate = f'2018-08-{day:02d}T23:59:59.999Z'
    newData = getData(plug,initialDate, finalDate, False)
    data.append(newData)
    day += 1

initialCost = 0
calculatedCost = 0
for i in range(len(data)):
    if(sum(data[i]) != 0):
        data[i] = Facade(data[i])
        initialCost += data[i].inputPrice
        for _ in range(50):
            data[i].nextGen()
        calculatedCost += data[i].getCost()
    else:
        data[i] = 0

print('The initial cost was: ', initialCost, ' €')
print('The cost calculated was: ', calculatedCost, ' €')

