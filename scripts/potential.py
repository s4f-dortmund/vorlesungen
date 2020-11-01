import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,2.0,1000)

a= 0.8
b= 4.0
c=-5.0
d = 0.2

y = a * x**4 +b * x**3 + c * x + d 

plt.plot(x,y, linewidth=5.0)
plt.axis('off')
plt.show()