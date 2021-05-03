# SPECTRAL Clustering
import matplotlib.pyplot as plt
import numpy as np

col1,col2,col3,col4 = np.loadtxt('fiber1',usecols=(1,2,3,4),unpack=True)
nrm1=1.0/(col1.max()-col1.min())
nrm2=1.0/(col2.max()-col2.min())
nrm3=1.0/(col3.max()-col3.min())
nrm4=1.0/(col4.max()-col4.min())

min1=col1.min()
min2=col2.min()
min3=col3.min()
min4=col4.min()

ggg=open('normalizations_fiber1','w')
ggg.write('%s\t%f\t%f\t%f\n' %(nrm1,nrm2,nrm3,nrm4))
ggg.write('%s\t%f\t%f\t%f\n' %(min1,min2,min3,min4))
ggg.close()

f=open('fiber1_norm.dat','w')
for i in range(len(col1)):
    col1_norm = (col1[i]-min1)*nrm1
    col2_norm = (col2[i]-min2)*nrm2
    col3_norm = (col3[i]-min3)*nrm3
    col4_norm = (col4[i]-min4)*nrm4
    
    f.write('%s\t%f\t%f\t%f\n' %(col1_norm,col2_norm,col3_norm,col4_norm))
    f.flush()
f.close()

#reading the normalized file
norm1,norm2,norm3,norm4 = np.loadtxt('fiber1_norm.dat',usecols=(0,1,2,3),unpack=(True))
X = np.column_stack((norm1,norm2,norm3,norm4))


from sklearn.cluster import SpectralClustering
# Applying the algorithm to the dataset
kmeans = SpectralClustering(n_clusters=3,affinity='nearest_neighbors')
y_kmeans = kmeans.fit_predict(X)
N_totale = X[y_kmeans == 0, 0].size + X[y_kmeans == 1, 0].size + X[y_kmeans == 2, 0].size 

N_1 = "{0:.3f}".format(X[y_kmeans == 0, 0].size*40.0/N_totale)
N_2 = "{0:.3f}".format(X[y_kmeans == 1, 0].size*40.0/N_totale)
N_3 = "{0:.3f}".format(X[y_kmeans == 2, 0].size*40.0/N_totale)

# re-applying the normalization factors 
for i in range(4):
    X[y_kmeans == i, 0] = X[y_kmeans == i, 0]/nrm1+min1
    X[y_kmeans == i, 1] = X[y_kmeans == i, 1]/nrm2+min2
    X[y_kmeans == i, 2] = X[y_kmeans == i, 2]/nrm3+min3
    X[y_kmeans == i, 3] = X[y_kmeans == i, 3]/nrm4+min4


plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0,1],s=8,facecolors='none', edgecolors='green',alpha=0.5,label='C1 ~'+N_1)
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1,1],s=8,facecolors='none', edgecolors='black',alpha=0.5,label='C2 ~'+N_2)
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2,1],s=8,facecolors='none', edgecolors='red',alpha=0.5,label='C3 ~'+N_3)

plt.xlim(-0.1,3.1)
plt.ylim(0,1.6)

plt.title('Clustering Fiber 1 ')
plt.xlabel('Coordination Number ')
plt.ylabel('Minimum distance')
plt.legend()
plt.savefig('fiber3.png')
plt.show()

a_file = open("C1.txt", "w")
b_file = open("C2.txt", "w")
c_file = open("C3.txt", "w")

np.savetxt(a_file, X[y_kmeans == 0,:])
np.savetxt(b_file, X[y_kmeans == 1,:])
np.savetxt(c_file, X[y_kmeans == 2,:])

a_file.close()
b_file.close()
c_file.close()

