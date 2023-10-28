# PCA BREAST CANCER
import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
# Load the Breast Cancer dataset
data = load_breast_cancer().data

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)
# Create a PCA instance with 2 components
n_components = 2
pca = PCA(n_components=n_components)
# Fit PCA to the scaled data
pca.fit(scaled_data)
# Transform the data to its principal components
transformed_data = pca.transform(scaled_data)
# Explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_variance_ratio)

# Principal components
principal_components = pca.components_
print("Principal Components:", principal_components)



# PCA ( IF BREAST CANCER DOESN'T WORK)
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset from the CSV file
data = pd.read_csv('data.csv')

# Step 2: Split the data into features (X) and target (y)
X = data.drop('target_column_name', axis=1)  # Replace 'target_column_name' with the actual target column name
y = data['target_column_name']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Standardize the data (mean = 0, variance = 1)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Step 5: Perform PCA on the training data
n_components = min(X_train.shape[0], X_train.shape[1])
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca = pca.transform(X_test_std)

# Step 6: Train a machine learning model (e.g., Random Forest) on the reduced-dimension data
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_pca, y_train)

# Step 7: Make predictions and evaluate the model
y_pred = clf.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


