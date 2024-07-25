#Line plot is used to display trends over time
import matplotlib.pyplot as plt
import pandas as pd

data = {'Month' :['Jan','Feb','Mar','Apr',"May"],
        'Sales': [100, 120 ,146, 130, 152]}

df = pd.DataFrame(data)

plt.plot(df['Month'],df['Sales'])
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')

plt.show( )