import pandas as pd
iris = pd.read_csv(r"C:\Users\pavan\Downloads\IRIS (1).csv")

x = iris.iloc[:,:-1].values
y = iris.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3)
y_pred = kmeans.fit_predict(x)
# print(kmeans.cluster_centers_)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[y_pred == 0,0], x[y_pred == 0,1], x[y_pred == 0,2], s=50, c='red', label='Setosa')
ax.scatter(x[y_pred == 1,0], x[y_pred == 1,1], x[y_pred == 1,2], s=50, c='green', label='Versicolor')
ax.scatter(x[y_pred == 2,0], x[y_pred == 2,1], x[y_pred == 2,2], s=50, c='blue', label='Verginica')
ax.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,2], s=150, c='yellow', label='Centroids')

plt.legend()
plt.show()

