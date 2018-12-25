# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:54:51 2018

@author: xingxf03
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

t = np.arange(0.0,5.0,0.01)
s = np.cos(2*np.pi*t)
line,= plt.plot(t,s,lw=2)
plt.annotate('local max',xy=(2,1),xytext=(3,1.5),
             arrowprops=dict(facecolor='black',shrink=0.05))
plt.ylim(-2,2)
#plt.show()
plt.show()

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
np.random.seed(196800)

y = np.random.normal(loc=0.5,scale=0.4,size=1000)
y = y[(y>0)&(y<1)]
y.sort()
x = np.arange(len(y))




plt.figure(1)

#linear
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

#log
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

#symmetric log
plt.subplot(223)
plt.plot(x,y,-y.mean())
plt.yscale('symlog',linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

#logit
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.subplots_adjust(
         top=0.92,
         bottom=0.008,
         left = 0.10,
         right = 0.95,
         hspace = 0.45,
         wspace = 0.55
        )
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles

plt.show()
