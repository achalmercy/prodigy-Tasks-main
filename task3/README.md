# Bank Marketing Dataset Classification Using Decision Tree

## Overview
This project implements a decision tree classifier on the Bank Marketing dataset. The objective is to predict whether a customer will subscribe to a term deposit based on their demographic and behavioral data. The project involves data preprocessing, handling categorical variables, addressing class imbalance, and evaluating the model's performance using metrics like precision, recall, and accuracy.

## Files
- `bank-additional-full.csv`: Extended dataset with additional features.
- `bank-full.csv`: Full version of the dataset.
- `bank.csv`: Smaller version of the dataset.
- `classification_report.txt`: File containing the model's evaluation metrics.
- `decision_tree_rules.txt`: File containing the textual representation of the decision tree.

## Prerequisites
Before running the script, ensure you have the following Python libraries installed:

- pandas
- numpy
- scikit-learn

Install missing dependencies using pip:
```bash
pip install pandas numpy scikit-learn
```

## How to Run
1. Clone or download this repository.
2. Place the Bank Marketing dataset files (`bank-additional-full.csv`, `bank-full.csv`, `bank.csv`) in the appropriate directory.
3. Run the Python script:
   ```bash
   python main.py
   ```

## Script Features
### Data Preprocessing
- Encodes categorical variables using `LabelEncoder`.
- Combines multiple datasets into a single DataFrame for analysis.
- Splits data into training and testing sets with an 80-20 ratio.

### Decision Tree Classifier
- Implements `DecisionTreeClassifier` with `class_weight='balanced'` to handle class imbalance.
- Predicts whether a customer will subscribe to a term deposit.

### Model Evaluation
- Generates a classification report with precision, recall, F1-score, and accuracy.
- Outputs decision tree rules in a readable format.

## Outputs
The script generates:
1. **Classification Report**: Saved to `classification_report.txt`.
2. **Decision Tree Rules**: Saved to `decision_tree_rules.txt`.

## Key Insights
- The decision tree effectively classifies the target variable but may struggle with imbalanced datasets.
- `class_weight='balanced'` improves prediction for minority classes.
- Additional feature engineering or resampling techniques could enhance model performance.

## Note
Ensure the Bank Marketing dataset files (`bank-additional-full.csv`, `bank-full.csv`, `bank.csv`) are in the correct directory before running the script.

## License
This project is for educational purposes and uses publicly available datasets from the UCI Machine Learning Repository.
