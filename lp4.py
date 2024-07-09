# SVM
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


data=load_breast_cancer()
x=data.data
y=data.target 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

svm=SVC(kernel='linear')
svm.fit(x_train,y_train)

y_pred=svm.predict(x_test)


accuracy=accuracy_score(y_test,y_pred)
print("PREDICTED:", y_pred)
print("CONFUSION MATRIX: \n",confusion_matrix(y_test,y_pred))
print("ACCURACY:",accuracy)
print(classification_report(y_test,y_pred))