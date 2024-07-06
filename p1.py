import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


data = pd.read_csv("diabetes_march24.csv")
print(data)

print(data.isnull().sum())

features = data[["FS","FU"]]
target = data[["Diabetes"]]

cfeatures = pd.get_dummies(features,drop_first=True)
print(features)
print(cfeatures)


x_train,x_test,y_train,y_test = train_test_split(cfeatures.values,target)


model = LogisticRegression()
model.fit(x_train,y_train)
cr = classification_report(y_test,model.predict(x_test))
print(cr)