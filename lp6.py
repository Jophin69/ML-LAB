#RANDOM FOREST CLASSIFIER
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report


data=load_breast_cancer()

x=data.data
y=data.target 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


clf=RandomForestClassifier(n_estimators=500,max_leaf_nodes=16,n_jobs=-1)

clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)


print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
