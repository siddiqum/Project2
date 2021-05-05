import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y, 'g--', label='2x')

# select interval we want to plot points at
x2 = np.arange(0,4.5,0.5)

# Plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2, 'b', label='X^2')

# Plot remainder of graph as a dot
plt.plot(x2[5:], x2[5:]**2, 'b--')

plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4,])

plt.legend()
plt.savefig('mygraph.png', dpi=300)
plt.show()