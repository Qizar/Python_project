import matplotlib.pyplot as plt

x = [i for i in range(101)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(x,y1)
ax1.set_title('Quadratic')
ax1.set_xlabel('X AXIS')
ax1.set_ylabel('Y AXIS')

ax2.plot(x,y2)
ax2.set_title('Cubic')
ax2.set_xlabel('X AXIS')
ax2.set_ylabel('Y AXIS')


