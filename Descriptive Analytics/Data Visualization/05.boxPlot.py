# Used to display the distribution of data based on a five-number summary 
# minimun
# first quartile
# median
# third quartile
# maximum

import matplotlib.pyplot as plt
import numpy as np

data =[np.random.randn(100) for _ in range(7)]

plt.boxplot(data)
plt.xlabel("Group")
plt.ylabel("Values")
plt.title("Boxplot of Random number")

plt.show()