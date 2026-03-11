import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("creditcard.csv")

# Display first 5 rows
print("First five rows of the dataset:")
print(df.head())

# Basic info
print("\nDataset Info:")
df.info()

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# Shape of data
print(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")

# Check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Class distribution
print("\nClass Distribution:")
print(df['Class'].value_counts())

# Visualize imbalance
plt.figure(figsize=(6,4))
sns.countplot(x='Class', data=df)
plt.title("Fraud vs Non-Fraud Transaction Counts")
plt.xlabel("Class (0 = Normal, 1 = Fraud)")
plt.ylabel("Count")
plt.show()
sns.set_theme(style="whitegrid")

# Distribution of transaction amounts
plt.figure(figsize=(8,5))
sns.histplot(df['Amount'], bins=100, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.show()

# Compare amount between normal and fraud
plt.figure(figsize=(8,5))
sns.boxplot(x='Class', y='Amount', data=df)
plt.title('Transaction Amounts by Class (0=Normal, 1=Fraud)')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df[df['Class'] == 0]['Time'], bins=100, color='green', label='Normal', alpha=0.6)
sns.histplot(df[df['Class'] == 1]['Time'], bins=100, color='red', label='Fraud', alpha=0.6)
plt.legend()
plt.title('Transaction Time Distribution (Normal vs Fraud)')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
corr = df.corr()

# Visualize with heatmap
plt.figure(figsize=(12,8))
sns.heatmap(corr, cmap='coolwarm', linewidths=0.2)
plt.title('Feature Correlation Heatmap')
plt.show()

# Correlation with target variable
corr_with_target = corr['Class'].sort_values(ascending=False)
print("\nCorrelation of features with 'Class':")
print(corr_with_target)

# Separate features (X) and target (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix (Logistic Regression)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Detailed report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# Initialize model
rf_model = RandomForestClassifier(
    n_estimators=100,       # number of decision trees
    random_state=42,
    class_weight='balanced' # handle class imbalance automatically
)

# Train on the scaled data
rf_model.fit(X_train_scaled, y_train)

y_pred_rf = rf_model.predict(X_test_scaled)
y_prob_rf = rf_model.predict_proba(X_test_scaled)[:, 1]

# Confusion Matrix
cm_rf = confusion_matrix(y_test, y_pred_rf)
print("Confusion Matrix:\n", cm_rf)

# Detailed metrics
print("\nClassification Report:\n", classification_report(y_test, y_pred_rf))

plt.figure(figsize=(5,4))
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Random Forest')
plt.show()
