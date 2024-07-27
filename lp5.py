# DECISION TREE
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
import matplotlib.pyplot as plt
from sklearn import tree 
data=load_iris()

x=data.data
y=data.target 


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

clf=DecisionTreeClassifier()

clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

plt.figure(figsize=(12,8))
tree.plot_tree(clf,feature_names=data.feature_names,class_names=data.target_names,filled=True)
plt.show()