import preprossessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# import pickle

X = preprossessing.X
Y = preprossessing.Y
sc = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

classifier= LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc = acc*100
print(f"Accuracy : ", acc)

# filename = 'LR.sav'
# pickle.dump(classifier, open(filename, 'wb'))
