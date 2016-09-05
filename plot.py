from prody import *
from matplotlib.pyplot import show
import numpy as np
import pandas as pd


class vector_generator:
    def __init__(self,PDBname):
        confProDy(auto_show=False)




confProDy(auto_show=False)


parse = parsePDB('5eh1')

hetero = parse.select('not protein and not nucleic and not water')

print len(hetero)


middle= calcCenter(hetero)

xx,yy,zz =np.meshgrid(np.arange(middle[0]-10,middle[0]+10,1),
                      np.arange(middle[1]-10,middle[1]+10,1),
                      np.arange(middle[2]-10,middle[2]+10,1))

# Upper left coordinate of drugs
vector = np.c_[xx.ravel(),yy.ravel(),zz.ravel()]

def inbox(tar,src,scale=1):
    if src[0]<= tar[0] and tar[0]<=src[0]+scale:
        if src[1]<= tar[1] and tar[1]<=src[1]+scale:
            if src[2]<= tar[2] and tar[2]<=src[2]+scale:
                return True
    return False


count = 0
collections = []
for pick_one in HierView(hetero).iterResidues():
    if pick_one.numAtoms()<=1 :
        continue

    collection = []
    xyz = pick_one.getCoords()
    middle = calcCenter(pick_one)
    scale=max(max(xyz[:,0])-middle[0],middle[0]-min(xyz[:,0]),
            max(xyz[:,1])-middle[1],middle[1]-min(xyz[:,1]),
            max(xyz[:,2])-middle[2],middle[2]-min(xyz[:,2]))
    assert scale<=20

    xx, yy, zz = np.meshgrid(np.linspace(middle[0] - 10, middle[0] + 10, 20),
                             np.linspace(middle[1] - 10, middle[1] + 10, 20),
                             np.linspace(middle[2] - 10, middle[2] + 10, 20))


    # Upper left coordinate of small cubics

    vector = np.c_[xx.ravel(), yy.ravel(), zz.ravel()]

    #print pick_one.getResname()
    num_vector = [0 for i in range(8000)]
    for atom in pick_one.iterAtoms():
        x,y,z= atom.getCoords()
        x_pos= int((x-vector[0][0])/1)
        if x_pos>=20:
            x_pos=19
        y_pos= int((y-vector[0][1])/1)
        if y_pos>=20:
            y_pos=19
        z_pos= int((z-vector[0][2])/1)
        if z_pos>=20:
            z_pos=19
        #print (x_pos,y_pos,z_pos)
        num_vector[x_pos*400+y_pos*20+z_pos]= atom.getIndex()
        collection.append([x_pos,y_pos,z_pos,atom.getIndex()])
    collections.append(collection)

    #This is how to get info from this data structure
    print pick_one.getResname()
    print pick_one.getChain()
    print num_vector



#for num,collection in enumerate(collections):
#    pd.DataFrame(columns=['x','y','z','index'],data = collection).to_csv('%s.csv'%str(num))



#plt = showProtein(MC3)
#show(plt)

'''for pick_one in HierView(hetero).iterResidues():
    plt = showProtein(pick_one)
    show(plt)
'''

