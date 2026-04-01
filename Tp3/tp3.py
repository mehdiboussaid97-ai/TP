import numpy as np
from matplotlib import pyplot as plt 

#%%
#Q1

def onde(A,c,lbda,x,t):
    '''
    A : Amplitude
    c : vitesse
    lbda : lambda
    x : position
    t : temp
    '''
    
    return A * (np.cos((( 2 * np.pi ) / lbda) * (x-c*t)))

#%%
#Q2
xx = np.linspace(-1, 1)
yy = []
for x in xx:
    yy = np.append(yy,onde(5, 1, 1, x, 0) )
    
print(xx,yy)    
plt.plot(xx, yy)
plt.show()

#%%
#Q3

tt = np.linspace(-1, 1,1000)
x1 = 0
x2 = np.pi/2
x3 = np.pi
x4 = 3 * np.pi/2
yy1 = []
yy2 = []
yy3 = []
yy4 = []
for t in tt:
    yy1 = np.append(yy1,onde(5, 1, 1, x1, t) )
    yy2 = np.append(yy2,onde(5, 1, 1, x2, t) )
    yy3 = np.append(yy3,onde(5, 1, 1, x3, t) )
    yy4 = np.append(yy4,onde(5, 1, 1, x4, t) )

figur = plt.figure()    
plt.subplot(2, 2,1)
plt.plot(tt, yy1)


plt.subplot(2, 2,2)
plt.plot(tt, yy2)

plt.subplot(2, 2,3)
plt.plot(tt, yy3)


plt.subplot(2, 2,4)
plt.plot(tt, yy4)

    