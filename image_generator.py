import matplotlib.pyplot as plt
import json

myfile = open('datasety/labirynt5x5.txt', 'r')
data = myfile.read().strip()
mazeMatrix = json.loads(data)

plt.imshow(mazeMatrix)
plt.show()
