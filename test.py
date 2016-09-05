import vector_gen
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib

generator = vector_gen.vector_generator('5eh1')

data_set =2


list = generator.get_one(data_set)

box = np.array(list).reshape([20,20,20])

scatter = [[i,j,k] for i in range(0,20) for j in range(0,20) for k in range(0,20) if box[i,j,k]!=0]


dic = {}

for i,j,k in scatter:
    dic[str(box[i,j,k])] = np.array([i,j,k]) + generator.middles[data_set]




boxes = np.array(scatter)

print boxes
boxes += generator.middles[data_set]
print boxes

boxess =  generator.raw_vectors[data_set]

print np.sort(boxess,axis=0)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = boxes[:,0]
ys = boxes[:,1]
zs = boxes[:,2]
ax.scatter(xs, ys, zs )


print boxes-np.sort(boxess,axis=0)

print dic
print generator.dictionary[data_set]


for key in dic:
    print dic[key] - generator.dictionary[data_set][key]

plt.show()