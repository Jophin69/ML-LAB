#NAIVE BAYES CLASSIFIER
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.metrics import accuracy_score,classification_report

data=fetch_20newsgroups_vectorized()

x=data.data
y=data.target 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

clf=MultinomialNB()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)


print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

