import numpy as np
from matplotlib import pyplot as plt 

#%%

def onde(A,c,lbda,x,t):
    '''
    A : Amplitude
    c : vitesse
    lbda : lambda
    x : position
    t : temp
    '''
    
    return A * (np.cos((( 2 * np.pi ) / lbda) * (x-c*t)))

xx = np.linspace(-10, 10)
yy = []
for x in xx:
    yy = np.append(yy,onde(5, 300, 20, x, 0) )
    
print(xx,yy)    
plt.plot(xx, yy)
plt.show()

