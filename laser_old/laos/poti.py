#!/usr/bin/python

import matplotlib.pyplot as plt




x = [0,    0.25, 0.5,  0.75,  1,  2,       3,     4,   5,   6,    7,8,9,10]
y = [0.04, 0.88, 1.51, 2.07, 2.41, 3.23, 3.66, 3.93, 4.11, 4.24, 4.34, 4.42, 4.49, 4.56]


fig = plt.figure()
plt.plot(x,y, 'x')
plt.xlabel("Umdrehungen")
plt.ylabel("Spannung [V]")
plt.savefig("poti.png")
