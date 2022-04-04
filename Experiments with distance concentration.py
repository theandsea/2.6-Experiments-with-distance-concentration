import math
import matplotlib.pyplot as plt
import numpy as np

def hist(x,d):
    title="histogram for the mutual distance for d="+str(d)+" n=100"
    plt.title(title)
    plt.ylabel("distance")
    plt.ylabel("frequency")
    plt.hist(x,bins=20,range=[0,2])
    plt.show()

def sph_sample(d,n):
    """
    generate n random points from d-dimensional sphere
    :param d:
    :param n:
    :return:
    """
    X_list=[]
    Z_list=[]
    for i in range(n):
        # normal dis
        Z=[]
        znorm=0
        for j in range(d):
            value=np.random.normal()
            Z.append(value)
            znorm+=value**2
        # normalize to sphere
        znorm=math.sqrt(znorm)
        X=[]
        for j in range(d):
            X.append(Z[j]/znorm) #
        X_list.append(X)

    return X_list

def dis_mutual(x):
    dislist=[]
    n=len(x)
    d=len(x[0])
    for i in range(n-1):
        a=x[i]
        for j in range(i+1,n):
            b=x[j]
            dissqr=0
            for k in range(d):
                dissqr += (a[k]-b[k])**2
            dislist.append(math.sqrt(dissqr))
    return dislist

def dis_euclidsqr(a,b,n):
    dissqr=0
    for k in range(n):
        dissqr += (a[k] - b[k]) ** 2
    # return math.sqrt(dissqr)
    return dissqr

def dis_minmax(x,d):
    minlist=[]
    maxlist=[]
    n=len(x)
    for i in range(1,n):
        print(i)
        mind=4
        maxd=0
        for j in range(i):
            dis=dis_euclidsqr(x[i],x[j],d)
            if mind>dis:
                mind=dis
            if maxd<dis:
                maxd=dis
            # mind=min(mind,dis)
            # maxd=max(maxd,dis)
        minlist.append(math.sqrt(mind))
        maxlist.append(math.sqrt(maxd))
    return [minlist,maxlist]

def fvalplt(y):
    x=np.arange(2, len(y[0]) + 2)
    plt.title("min and max distance for i from 1-(i-1)")
    plt.xlabel("index")
    plt.ylabel("distance")
    colval = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for i in range(len(y)):
        plt.plot(x, y[i], color=colval[i])
    plt.show()

"""
d=[2,5,10,20,100]
for i in range(5):
    x=sph_sample(d[i],100)
    dislist=dis_mutual(x)
    hist(dislist,d[i])
"""

d=1000
x=sph_sample(d,10000) # it seems that only d is large enough, it will concentrate
minmaxlist=dis_minmax(x,d)
fvalplt(minmaxlist)

