import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils.validation import check_is_fitted

# อ่านไฟล์ CSV ที่เก็บข้อมูลรถ
cars = pd.read_csv('cars.csv')

# แยกข้อมูล features กับ label
X = cars[['Horsepower', 'Seats']]
y = cars['CarType']

# แบ่งข้อมูลเป็น train set และ test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# สร้างโมเดล Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train โมเดล
clf.fit(X_train,y_train)
pred = (120,2)
pred1 = np.asarray(pred)
pred2 = pred1.reshape(1,-1)
realpre = clf.predict(pred2)
print(realpre[0])