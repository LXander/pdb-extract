import vector_gen
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib

generator = vector_gen.vector_generator('5eh1')


list = generator.get_one(2)

boxes = generator.raw_vectors[2]
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
xs = boxes[:,0]
ys = boxes[:,1]
zs = boxes[:,2]
ax.scatter(xs, ys, zs )

plt.show()