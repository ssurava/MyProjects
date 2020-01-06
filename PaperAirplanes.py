import numpy as np
import matplotlib.pyplot as plt 
betterplane =np.array([31,122,176,160,202,161,223,134,182,78,123,77,142,121,152,135,158,244,211,232,77,204,250,212,242])
simpleplane= np.array([141.9,55,95,150,231,231,282,243,102,347,70,212,173,162,158,251,278,222,216,264,96,45,37,235,158])
plt.boxplot([betterplane,simpleplane])
plt.xlabel("Planes: Simple(1) and Betterplane(2)")
plt.ylabel("Distance Traveled")
plt.title("Plane Oragami versus Distance Traveled")
fig= plt.figure()
fig.savefig('Planes.jpg')
