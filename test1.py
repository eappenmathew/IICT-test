#%matplotlib inline
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('brain.csv')
#print(data.shape)
#data


x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values

mean_x = np.mean(x)
mean_y = np.mean(y)

n =len(x)
numer=0
denom=0
for i in range(n):
  numer += (x[i]-mean_x)*(y[i]-mean_y)
  denom += (x[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(mean_x*b1)
print(b1,b0)


max_x = np.max(x) + 100
min_x = np.min(x) + 100
plt.scatter(x, y, c='#ef5323',label='Sac point')
x=np.linspace(min_x,max_x,1000)
y=b0+b1*x

plt.plot(x, y, c='#565656',label='Reg line')

plt.xlabel('Head size in cm3')
plt.ylabel('Brain weight in g')
plt.legend()
plt.show()
