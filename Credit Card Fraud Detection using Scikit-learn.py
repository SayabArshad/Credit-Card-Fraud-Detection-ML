#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

#load dataset

df = pd.read_csv(r"D:\python_ka_chilla\AI Projects\Credit Card Fraud Detection using Scikit-learn\creditcard.csv")


#display first few rows
print(df.head())
print(df.info())
print(df['Class'].value_counts())

#separate features and target variable
X = df.drop('Class', axis=1)
y = df['Class']

#split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets.")

#feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("Feature scaling completed.")

#create and train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained.")

#make predictions

y_pred = model.predict(X_test)
print("Predictions made.")

#evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.4f}')
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)
