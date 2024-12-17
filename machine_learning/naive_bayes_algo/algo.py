# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# # Load the dataset from CSV file
# data = pd.read_csv('DATA.csv')

# # Encode categorical data into numeric values
# label_encoders = {}
# for column in data.columns:
#     le = LabelEncoder()
#     data[column] = le.fit_transform(data[column])
#     label_encoders[column] = le

# # Separate features (X) and target (y)
# X = data.drop('PLAY', axis=1)  # All columns except 'PLAY'
# y = data['PLAY']  # Target column

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize the Naive Bayes classifier
# nb_classifier = GaussianNB()

# # Train the model on the training set
# nb_classifier.fit(X_train, y_train)

# # Predict on the test set
# y_pred = nb_classifier.predict(X_test)

# # Calculate the accuracy
# accuracy = accuracy_score(y_test, y_pred)

# print(f"Accuracy of Naive Bayes Classifier: {accuracy:.2f}")
import os
print(os.path.exists('DATA.csv/data'))  # Should print True if the file exists
