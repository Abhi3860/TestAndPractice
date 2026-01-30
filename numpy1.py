import numpy as np
import math
import matplotlib.pyplot as plt

a=np.linspace(0,100,33)


a1=np.arange(27).reshape(3,3,3)
#print(a1[0,:,:])

a2=np.arange(27).reshape(3,3,3)
#print(a1[0,0::2,:])

b1=np.arange(12).reshape(4,3)
b2=np.arange(12,24).reshape(4,3)
#print(np.vstack((b1,b2)))

#print(np.hsplit(b1,3))

