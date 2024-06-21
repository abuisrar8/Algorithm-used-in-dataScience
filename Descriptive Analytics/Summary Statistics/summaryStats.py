import pandas as pd

data ={'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9]}
data = pd.DataFrame(data)

mean = data.mean()
meadian = data.median()
mode = data.mode()
variance = data.var()

print(f"mean : \n{mean} \n")
print(f"meadian : \n{meadian} \n")
print(f"mode : \n{mode} \n")
print(f"variance : {variance} \n")