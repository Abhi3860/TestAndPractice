import numpy as np

a=np.linspace(0,100,33)


a1=np.arange(27).reshape(3,3,3)
#print(a1[0,:,:])

a2=np.arange(27).reshape(3,3,3)
#print(a1[0,0::2,:])

b1=np.arange(12).reshape(4,3)
b2=np.arange(12,24).reshape(4,3)
#print(np.vstack((b1,b2)))

#print(np.hsplit(b1,3))

c1=np.arange(27).reshape(3,3,3)
#print(c1[0,[0,1]])

c2=np.random.randint(0,200,36).reshape(6,6)
#print(c2[(c2>35) & (c2%2==0)])

