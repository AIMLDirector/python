from sklearn.datasets import load_iris
iris_data = load_iris()
X, Y= iris_data.data, iris_data.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=3)

from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors=3)
x_training_data = knn.fit(X_train, Y_train)
print(x_training_data)
Y_pred = knn.predict(X_test)
print("predicted target No:", Y_pred)
print("Real target no:", Y_test)
from sklearn import metrics
print("KNN model accuracy", metrics.accuracy_score(Y_test, Y_pred))


