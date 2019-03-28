import requests

URL = 'http://localhost:8080/data'

#r = requests.get(URL)
data = str(requests.get(URL).content)
data = data.split('\\n')

avg = []
sum = 0
for i in range(len(data)):
    if i%15 == 0:
        sum += float(data[i].split(',')[2])
        avg.append(sum / 15)
        sum = 0
    else:
        sum += float(data[i].split(',')[2])

print()
