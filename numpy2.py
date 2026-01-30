import numpy as np
import math
import matplotlib.pyplot as plt




c1=np.arange(27).reshape(3,3,3)
#print(c1[0,[0,1]])

c2=np.random.randint(0,200,36).reshape(6,6)
#print(c2[(c2>35) & (c2%2==0)])

def sigmoid(array):
    return 1/(1+np.exp((array)))

c3=np.arange(12)
#print(sigmoid(c3))


p1=np.linspace(-10,10,100)
p2=p1
#plt.plot(p1,p2)
#plt.show()