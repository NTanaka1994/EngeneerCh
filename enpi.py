import numpy as np

x=np.arange(0,1.01,0.01)
y=np.sqrt(1-x**2)
total=0
for i in range(len(x)-1):
    if i!=99 or i!=100:
        total=total+(x[i+1]-x[i])*(y[i]+y[i+1])/2
    
print(total*4)
