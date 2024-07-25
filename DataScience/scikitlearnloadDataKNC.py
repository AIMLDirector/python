from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris_dataset = load_iris()
print("print iris keys:{}".format(iris_dataset.keys()))
#print("print iris data:{}".format(iris_dataset['data']))
print("print iris data shape :{}".format(iris_dataset['data'].shape))
print("print iris target :{}".format(iris_dataset['target']))
#print("print iris target shape :{}".format(iris_dataset['target'].shape))
print("print iris target name  :{}".format(iris_dataset['target_names']))
X= iris_dataset.data
y = iris_dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, roc_curve

# making predictions on the testing set
y_pred = knn.predict(X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print("KNN model accuracy", metrics.accuracy_score(y_test, y_pred))

# making prediction for out of sample data
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = knn.predict(sample)
pred_species = [iris_dataset.target_names[p] for p in preds]
print("Predictions", pred_species)