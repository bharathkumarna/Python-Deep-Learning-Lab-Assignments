import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

winedataset = datasets.load_wine()
x = winedataset.data[:,:2]
y = winedataset.target

h=0.3
xmin, xmax = x[:, 0].min() - 1, x[:, 0].max() + 1
ymin, ymax = x[:, 1].min() - 1, x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(xmin, xmax, h),
                     np.arange(ymin, ymax, h))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model = svm.SVC()

predictions_linear = model.set_params(kernel='linear').fit(x_train, y_train).predict(x_test)

predictions_rbf = model.set_params(kernel='rbf').fit(x_train, y_train).predict(x_test)

accuracy_linear = metrics.accuracy_score(y_test,predictions_linear)
accuracy_rbf = metrics.accuracy_score(y_test,predictions_rbf)

print("Accuracy with kernel=linear:",accuracy_linear)
print("Accuracy with kernel=rbf:",accuracy_rbf)
