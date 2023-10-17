import pandas as pd
import preprossessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import (SMOTE, RandomOverSampler)
# import pickle

X = preprossessing.X
Y = preprossessing.Y

oversampled = SMOTE()
X, Y= oversampled.fit_resample(X, Y)
X = pd.DataFrame(X, columns=['age', 'failures', 'absences', 'school', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian','traveltime', 'studytime', 'schoolsup', 'famsup', 'paid', 'activities','nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime','goout', 'Dalc', 'Walc', 'health', 'G1', 'G2'])
Y = pd.DataFrame(Y, columns=['Classes'])

sc = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size= 0.3, random_state=0)

x_train = x_train[['G2','G1','absences','goout','Walc','age','famrel','Mjob','reason','studytime','Medu','health','freetime','Fedu','Fjob','Dalc','traveltime','famsize','paid','failures','guardian','sex','activities','famsup','romantic','nursery','address','internet','Pstatus','schoolsup','school']]
x_test = x_test[['G2','G1','absences','goout','Walc','age','famrel','Mjob','reason','studytime','Medu','health','freetime','Fedu','Fjob','Dalc','traveltime','famsize','paid','failures','guardian','sex','activities','famsup','romantic','nursery','address','internet','Pstatus','schoolsup','school']]

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train.values.ravel())
y_pred = knn.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc = acc*100
print(f"Accuracy : ", acc)

# filename = 'KNN_SM_FS.sav'
# pickle.dump(knn, open(filename, 'wb'))