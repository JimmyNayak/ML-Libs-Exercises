from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

ds = datasets.load_iris()

# print(ds)

model = SVC(gamma='auto')
model.fit(ds.data, ds.target)
#
# print(model)

expected = ds.target
# print(expected)


predicted = model.predict(ds.data)
# print(predicted)
# print(metrics.classification_report(expected, predicted))

# KNN (K Nearest Neighbors) Algorithm

x = ds.data
y = ds.target

print(x.shape)
print(y.shape)

knn = KNeighborsClassifier(n_neighbors=1)

print(knn)

knn.fit(x, y)

a = np.array([2, 4, 5, 6])

prediction = knn.predict([a])

print(knn.predict([a]))

print(ds['target_names'][prediction])
