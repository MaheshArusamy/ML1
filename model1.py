import pandas as pd
from sqlalchemy import values
data=pd.read_csv("C:\ML1\Dataset\employees.csv")
print(data)

print(data.head())
print(data.isnull().sum())
print(data.isnull().sum().sum())

data=data.dropna(subset=["working"])
numerical_columns=["experience","attendance","performance"]
for column in numerical_columns:
    data[column]=data[column].fillna(data[column].median())
print(data)

print(data.isnull().sum())

print(data.duplicated().sum())

#to remove duplicate values
data=data.drop_duplicates()

#save the cleaned data to a new CSV file
data.to_csv("C:\ML1\Dataset\employees_cleaned.csv", index=False)  
print("data saved ")

#to convert working values to binary values
data['working'] = data['working'].map({'Good': 1, 'Poor': 0})
print(data)

x=data[['experience','attendance','performance']]
y=data['working']
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
print("model trained")

y_pred=model.predict(x_test)
print(y_test.values)
print(y_pred)

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
accuracy=accuracy_score(y_test,y_pred)
print("accuracy:", accuracy * 100, "%")
print(classification_report(y_test, y_pred,zero_division=0))

import joblib
joblib.dump(model, "C:\\ML1\\model\\employee_model.pkl")
print("model saved")

import joblib
import pandas as pd
model=joblib.load("C:\\ML1\\model\\employee_model.pkl")
new_employee_data=pd.DataFrame({ 'experience':[1],"attendance":[50],"performance":[55]})
prediction=model.predict(new_employee_data)
if prediction[0]==1:
    print("The employee is working well.")
else:
    print("The employee is not working well.")