from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import numpy as np
import pandas as pd

data = pd.read_csv("../final_dataset/final_part4.csv")

data = data.rename(columns = {"Recession State": "target"})

Y = data.target

data = data.drop(['target'], axis = 1)
data = data.drop(['DATE'], axis = 1)

X = data.values.tolist()

X, Y = shuffle(X,Y)
x_train = []
y_train = []
x_test = []
y_test = []

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.75)

print(x_train)
print("#################################################################")
print(y_train)


svclassifier = SVC(kernel='linear', C=1, gamma='auto')
svclassifier.fit(x_train, y_train)

y_pred = svclassifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

print(svclassifier.score(x_test, y_test))
# from sklearn.model_selection import cross_val_score
#
# scores = cross_val_score(svclassifier, X, Y, cv=5)
#
# print(scores)