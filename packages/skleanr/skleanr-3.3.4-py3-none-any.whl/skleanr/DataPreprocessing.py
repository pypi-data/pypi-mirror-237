import pandas as pd
from sklearn.impute import SimpleImputer
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder

# # Create the DataFrame
# data = {
#  'Student ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  'Exam 1 Score': [85, 76, 90, 65, 88, None, 78, 92, 85, 70],
#  'Exam 2 Score': [92, 78, 88, 75, 91, 82, 76, 96, 89, 68],
#  'Exam 3 Score': [88, None, 94, 80, 87, 79, 72, 98, 91, 75],
#  'Final Grade': ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'A', 'B']
# }
# df = pd.DataFrame(data)
# Save to CSV
# df.to_csv('your_dataset.csv', index=False)

# Import the DataFrame
df = pd.read_csv('your_dataset.csv')

print("Dataset:\n", df)
print("\n\n\n\n")

# Imputation
df1 = df.copy()  # Create a copy to avoid modifying the original DataFrame
imputer = SimpleImputer(strategy="mean")
df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']] = imputer.fit_transform(df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']])
print("Imputation:\n", df1)
print("\n\n\n\n")

# Anomaly Detection
z_scores = stats.zscore(df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']])
threshold = 3
outliers = (abs(z_scores) > threshold).any(axis=1)
df1['Is Outlier'] = outliers
print("Anomaly Detection:\n", df1)
print("\n\n\n\n")

# Standardization
scaler = StandardScaler()
df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']] = scaler.fit_transform(df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']])
print("Standardization:\n", df1)
print("\n\n\n\n")

# Normalization
scaler = MinMaxScaler()
df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']] = scaler.fit_transform(df1[['Exam 1 Score', 'Exam 2 Score', 'Exam 3 Score']])
print("Normalization:\n", df1)
print("\n\n\n\n")

# Encoding (if applicable)
# Assuming 'Categorical_Column' is the name of the column you want to encode
if 'Exam 1 Score' in df1:
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(df1[['Exam 1 Score']].values.reshape(-1, 1)).toarray()
    encoded_columns = encoder.get_feature_names_out(['Exam 1 Score'])
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
    df1 = pd.concat([df1, encoded_df], axis=1)
    df1.drop(['Exam 1 Score'], axis=1, inplace=True)

print("Encoding:\n", df1)
print("\n\n\n\n")

# Output
print("Final Preprocessed Dataset:\n", df1)
