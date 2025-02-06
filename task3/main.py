import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# File paths
file_paths = ['bank-additional-full.csv', 'bank-full.csv', 'bank.csv']

# Load datasets and combine them
try:
    dfs = [pd.read_csv(file, sep=';') for file in file_paths]
    data = pd.concat(dfs, ignore_index=True)
    print("Datasets loaded and combined successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Preprocessing
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Define features (X) and target (y)
X = data.drop(columns=['y'])
y = data['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Classifier with class weights
clf = DecisionTreeClassifier(random_state=42, class_weight='balanced')
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# Visualize the decision tree structure (text representation)
tree_rules = export_text(clf, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n", tree_rules)
