# Used to compare quantities of different categories

import matplotlib.pyplot as plt

categories = ['A','B','C','D']
values = [10,23,17,5]

plt.bar(categories,values)
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Category Values')

plt.show()  