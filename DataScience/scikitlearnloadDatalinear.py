from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
iris_dataset = load_iris()
X= iris_dataset.data
y = iris_dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)