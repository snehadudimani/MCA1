import pandas as pd
import preprossessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import (SMOTE, RandomOverSampler)
import pickle

X = preprossessing.X
Y = preprossessing.Y
sc = StandardScaler()

oversampled = SMOTE()
X, Y= oversampled.fit_resample(X, Y)
X = pd.DataFrame(X, columns=['age', 'failures', 'absences', 'school', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian','traveltime', 'studytime', 'schoolsup', 'famsup', 'paid', 'activities','nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime','goout', 'Dalc', 'Walc', 'health', 'G1', 'G2'])
Y = pd.DataFrame(Y, columns=['Classes'])

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

x_train = x_train[['G2', 'G1', 'absences', 'goout', 'Walc', 'age', 'famrel', 'Mjob','reason','studytime','Medu','health','freetime','Fedu','Fjob','Dalc','traveltime','famsize','paid','failures','guardian','sex','activities','famsup','romantic','nursery','address','internet','Pstatus','schoolsup','school']]
x_test = x_test[['G2','G1','absences','goout','Walc','age','famrel','Mjob','reason','studytime','Medu','health','freetime','Fedu','Fjob','Dalc','traveltime','famsize','paid','failures','guardian','sex','activities','famsup','romantic','nursery','address','internet','Pstatus','schoolsup','school']]

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


rdecision_tree = RandomForestClassifier(n_estimators=100)
rf = rdecision_tree.fit(x_train, y_train.values.ravel())
y_pred = rf.predict(x_test)


acc = accuracy_score(y_test, y_pred)
acc = acc*100
print(f"Accuracy : ", acc)

filename = 'RF_SM_FS.sav'
pickle.dump(rf, open(filename, 'wb'))