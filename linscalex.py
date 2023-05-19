import matplotlib.pyplot as plt
import numpy as np

b = 2.  # Try 100. too
t = 1.

# Define some curves:
x = np.linspace(0.1,3.,100)
y1 = x
y2 = x**2
y3 = np.exp(x)/2.
y4 = np.log(x)*2.

plt.figure()

plt.subplot(1,3,1)
plt.title('base 10 default')
plt.ylim(-100,100)
plt.yscale('symlog',linthreshy=t)               # should set decade = half-linear
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.subplot(1,3,2)
plt.title('base 10 smooth?')
plt.ylim(-100,100)
plt.yscale('symlog',linthreshy=t,linscaley=np.log10(np.e))      # smooth match?
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.subplot(1,3,3)
plt.title('base %d default' % (b))
plt.ylim(-100,100)
plt.yscale('symlog',linthreshy=t,basey=b)       # doesn't set decade or b-ade = half-linear
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.show()