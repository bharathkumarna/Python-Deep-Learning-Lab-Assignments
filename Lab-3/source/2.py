from collections import OrderedDict
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

i = []
s = []

def get_data(filename):
    with open(filename,'r') as csvdocument:
        csvFileContent = csv.reader(csvdocument)
        next(csvFileContent)  # skipping column names
        for row in csvFileContent:
            i.append(int(row[3]))
            s.append(int(row[4]))
    return

get_data('datasets/Customers.csv')
data = list(zip(i,s))
print("Data:")
print(data)

kmeans = KMeans(n_clusters=5)
kmeans.fit(data)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print("Centroids:")
print(centroids)

colors = ["y","g","b","r","c"]
label = ["Cluster-1","Cluster-2","Cluster-3","Cluster-4","Cluster-5"]
#plot points
for i in range(len(data)):
    print("coordinate:",data[i], "label:", labels[i])
    plt.scatter(data[i][0], data[i][1], c = colors[labels[i]], label = label[labels[i]])
#plot centroids
plt.scatter(centroids[:, 0],centroids[:, 1], label = "Centroids",marker = "x", s=150, linewidths = 10, zorder = 15)
plt.title('clusters of customers')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
#remove duplicates of labels
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.show()
#predictions
print("Predicted Class:")
print(kmeans.predict([(20,40)]))