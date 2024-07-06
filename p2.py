import pandas as pd
from sklearn.linear_model import LogisticRegression
from pickle import*

data = pd.read_csv("diabetes_march24.csv")

features = data[["FS","FU"]]
target = data[["Diabetes"]]

cfeatures = pd.get_dummies(features,drop_first=True)

model = LogisticRegression()
model.fit(cfeatures.values,target)

f =open("dia.pkl","wb")
dump(model,f)
f.close()
print("model created")