import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# loading dataset 
iris = load_iris()
X = iris.data
y = iris.target

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.5)

# build the model
classifier = RandomForestClassifier(n_estimators=10)

# train the classifier
classifier.fit(X_train, y_train)

#predictions
predicted = classifier.predict(X_test)

# check accuracy
print(accuracy_score(predicted, y_test))
