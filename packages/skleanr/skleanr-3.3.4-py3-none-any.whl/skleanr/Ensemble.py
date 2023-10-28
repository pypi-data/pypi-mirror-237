from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Breast Cancer Wisconsin dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define base estimators
base_estimators = [
    ('decision_tree', DecisionTreeClassifier()),
    ('random_forest', RandomForestClassifier()),
    ('svm', SVC())
]

# Create a StackingClassifier with a meta-learner (e.g., Decision Tree Classifier)
stacking_classifier = StackingClassifier(estimators=base_estimators, final_estimator=DecisionTreeClassifier(), cv=5)

# Fit the ensemble model on the training data
stacking_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = stacking_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy = accuracy*100
print(f"Accuracy: {accuracy:}")