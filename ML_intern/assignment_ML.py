#seperating category and data from documents
fd=open('trainingdata.txt',"r+")
fd.readline()
fw=open('trd.txt',"w+")
for i in range(54854):
    text=fd.readline()
    text=text.replace(" ","\t",1)
    fw.write(text)
fd.close()
fw.close()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('trd.txt', delimiter = '\t', quoting = 3)

#bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
Y=dataset.iloc[:,0].values
x = dataset.iloc[:, 1].values
X = cv.fit_transform(x).toarray()


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)

# using Naive Bayes 
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting 
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
