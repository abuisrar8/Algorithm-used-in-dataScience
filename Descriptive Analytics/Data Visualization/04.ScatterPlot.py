# Used to display the relationship between two variables

import matplotlib.pyplot as plt
import numpy as np
x= np.random.random_integers(1,60,20)
y= np.random.random_integers(1,60,20)

plt.scatter(x,y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot ")

plt.show()