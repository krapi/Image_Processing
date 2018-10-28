import matplotlib.pyplot as plt
import numpy as np




t = np.arange(0,10,0.01)
plt.figure()
sine = np.sin(2*np.pi*t)
cosine = np.cos(2*np.pi*t)
exponential = np.exp(t)
l1, = plt.plot(t, sine, label='Sine')
l3, = plt.plot(t, cosine , label='cosine')
l2, = plt.plot(t, exponential, label='Exponential')
l4, = plt.plot(t, sine * exponential, label='Sine * Exponential')
l5, = plt.plot(t, cosine + exponential, label='Cosine + Exponential')
plt.xlabel("time ->")
plt.ylabel("amplitude ->")
plt.ylim(-20,20)
plt.legend(handles=[l1, l2, l3, l4,l5], loc=0)
plt.show()
x = np.arange(-1, 2, 0.01)
y = (x >= 0)
plt.plot(x, y)
plt.title("Unit step signal")
plt.show()
