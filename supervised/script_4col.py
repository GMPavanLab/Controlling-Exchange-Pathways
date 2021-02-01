"""

Created on Tue Oct 9 11:30:34 2018
@author: ALDM

"""

# K-Means Clustering
import matplotlib.pyplot as plt
import numpy as np
col1,col2,col3,col5 = np.loadtxt('NNN042',usecols=(1,2,3,4),unpack=True)
nrm1=1.0/(col1.max()-col1.min())
nrm2=1.0/(col2.max()-col2.min())
nrm3=1.0/(col3.max()-col3.min())
nrm4=1.0/(col5.max()-col5.min())


min1=col1.min()
min2=col2.min()
min3=col3.min()
min4=col5.min()
f=open('norm.dat','w')
for i in range(len(col1)):
    col1_norm = (col1[i]-min1)*nrm1
    col2_norm = (col2[i]-min2)*nrm2
    col3_norm = (col3[i]-min3)*nrm3
    col5_norm = (col5[i]-min4)*nrm4
    
    f.write('%s\t%f\t%f\t%f\n' %(col1_norm,col2_norm,col3_norm,col5_norm))
    f.flush()
f.close()
 
norm1,norm2,norm3,norm5 = np.loadtxt('norm.dat',usecols=(0,1,2,3),unpack=(True))
X = np.column_stack((norm1,norm2,norm3,norm5))


# Using the elbow method to find  the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=5000,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Applying k-means to the dataset
kmeans = KMeans(n_clusters=4,init='k-means++',max_iter=5000,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(X)
N_totale = X[y_kmeans == 0, 0].size + X[y_kmeans == 1, 0].size + X[y_kmeans == 2, 0].size + X[y_kmeans == 3, 0].size

N_1 = "{0:.3f}".format(X[y_kmeans == 0, 0].size*40.0/N_totale)
N_2 = "{0:.3f}".format(X[y_kmeans == 1, 0].size*40.0/N_totale)
N_3 = "{0:.3f}".format(X[y_kmeans == 2, 0].size*40.0/N_totale)
N_4 = "{0:.3f}".format(X[y_kmeans == 3, 0].size*40.0/N_totale)

# Visualising the clusters
#print X[y_kmeans == 3, 0]/nrm1+min1 , X[y_kmeans == 3, 0]*(col1.max()-col1.min())+col1.min()

plt.scatter(X[y_kmeans == 3, 0]/nrm1+min1, X[y_kmeans == 3,1]/nrm2+min2,s=5,c='red',label='C4 ~'+N_4)
plt.scatter(X[y_kmeans == 1, 0]/nrm1+min1, X[y_kmeans == 1,1]/nrm2+min2,s=5,c='green',label='C2 ~'+N_2)
plt.scatter(X[y_kmeans == 0, 0]/nrm1+min1, X[y_kmeans == 0,1]/nrm2+min2,s=5,c='blue',label='C1 ~'+N_1)
plt.scatter(X[y_kmeans == 2, 0]/nrm1+min1, X[y_kmeans == 2,1]/nrm2+min2,s=5,c='black',label='C3 ~'+N_3)
plt.title('Clustering Fibra C5 - usando 3 variabili e proiettando su 2')
plt.xlabel('coord')
plt.ylabel('mindist')
plt.legend()
#plt.axis([min1, col1.max(), min2, col2.max()])
plt.savefig('040')
plt.show()

plt.scatter(X[y_kmeans == 3, 0]*(col1.max()-col1.min())+col1.min(), X[y_kmeans == 3,2]*(col3.max()-col3.min())+col3.min(),s=5,c='red',label='C4 ~'+N_4)
plt.scatter(X[y_kmeans == 1, 0]*(col1.max()-col1.min())+col1.min(), X[y_kmeans == 1,2]*(col3.max()-col3.min())+col3.min(),s=5,c='green',label='C2 ~'+N_2)
plt.scatter(X[y_kmeans == 0, 0]*(col1.max()-col1.min())+col1.min(), X[y_kmeans == 0,2]*(col3.max()-col3.min())+col3.min(),s=5,c='blue',label='C1 ~'+N_1)
plt.scatter(X[y_kmeans == 2, 0]*(col1.max()-col1.min())+col1.min(), X[y_kmeans == 2,2]*(col3.max()-col3.min())+col3.min(),s=5,c='black',label='C3 ~'+N_3)
plt.title('Clustering Fibra C5 - usando 3 variabili e proiettando su 2')
plt.xlabel('coord')
plt.ylabel('contacts')
plt.legend()
#plt.axis([col1.min(), col1.max(), col3.min(), col3.max()])
plt.show()


plt.scatter(X[y_kmeans == 3, 2]*(col3.max()-col3.min())+col3.min(), X[y_kmeans == 3,1]*(col2.max()-col2.min())+col2.min(),s=5,c='red',label='C4 ~'+N_4)
plt.scatter(X[y_kmeans == 1, 2]*(col3.max()-col3.min())+col3.min(), X[y_kmeans == 1,1]*(col2.max()-col2.min())+col2.min(),s=5,c='green',label='C2 ~'+N_2)
plt.scatter(X[y_kmeans == 0, 2]*(col3.max()-col3.min())+col3.min(), X[y_kmeans == 0,1]*(col2.max()-col2.min())+col2.min(),s=5,c='blue',label='C1 ~'+N_1)
plt.scatter(X[y_kmeans == 2, 2]*(col3.max()-col3.min())+col3.min(), X[y_kmeans == 2,1]*(col2.max()-col2.min())+col2.min(),s=5,c='black',label='C3 ~'+N_3)
plt.title('Clustering Fibra C5 - usando 3 variabili e proiettando su 2')
plt.xlabel('contacts')
plt.ylabel('mindist')
plt.legend()
#plt.axis([col3.min(), col3.max(), col2.min(), col2.max()])
plt.show()


plt.scatter(X[y_kmeans == 3, 1]*(col2.max()-col2.min())+col2.min(), X[y_kmeans == 3,3]*(col5.max()-col5.min())+col5.min(),s=5,c='red',label='C4 ~'+N_4)
plt.scatter(X[y_kmeans == 1, 1]*(col2.max()-col2.min())+col2.min(), X[y_kmeans == 1,3]*(col5.max()-col5.min())+col5.min(),s=5,c='green',label='C2 ~'+N_2)
plt.scatter(X[y_kmeans == 0, 1]*(col2.max()-col2.min())+col2.min(), X[y_kmeans == 0,3]*(col5.max()-col5.min())+col5.min(),s=5,c='blue',label='C1 ~'+N_1)
plt.scatter(X[y_kmeans == 2, 1]*(col2.max()-col2.min())+col2.min(), X[y_kmeans == 2,3]*(col5.max()-col5.min())+col5.min(),s=5,c='black',label='C3 ~'+N_3)
plt.title('Clustering Fibra C5 - usando 3 variabili e proiettando su 2')
plt.xlabel('coord')
plt.ylabel('min dip')
plt.legend()
#plt.axis([col1.min(), col1.max(), col5.min(), col5.max()])
plt.show()


