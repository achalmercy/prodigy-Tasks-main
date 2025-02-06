# Titanic Data Cleaning and Exploratory Data Analysis (EDA)

## Overview
This project performs data cleaning and exploratory data analysis (EDA) on the Titanic dataset. The goal is to clean the dataset by handling missing values, dropping unnecessary columns, and exploring the relationships between variables to identify patterns and trends.

## Files
- `train.csv`: Training dataset containing passenger information, survival status, and features.
- `test.csv`: Testing dataset for predictions (not used in this project).
- `gender_submission.csv`: Example submission file (not used in this project).

## Prerequisites
Before running the script, ensure you have the following Python libraries installed:

- pandas
- numpy
- seaborn
- matplotlib

Install missing dependencies using pip:
```bash
pip install pandas numpy seaborn matplotlib
```

## How to Run
1. Clone or download this repository.
2. Place the Titanic dataset files (`train.csv`, `test.csv`, `gender_submission.csv`) in the appropriate directory.
3. Run the Python script:

```bash
python task2.py
```

## Script Features
### Data Cleaning
- Fills missing values in the `Age` column with the median.
- Fills missing values in the `Embarked` column with the mode.
- Drops columns `Cabin`, `Name`, and `Ticket` due to high missing values or irrelevance to analysis.

### Exploratory Data Analysis (EDA)
The script generates visualizations and statistical summaries to uncover insights:
- Survival distribution.
- Survival by passenger class (`Pclass`).
- Age distribution with survival status.
- Fare distribution by passenger class.
- Correlation heatmap of numeric features.

### Key Insights
1. Most passengers did not survive.
2. Higher survival rates observed for passengers in 1st class.
3. Younger passengers (children) show higher survival rates.
4. Fare is positively correlated with survival.

## Output
The script generates:
- Count plots of survival status and class-wise survival.
- Histograms of age distribution.
- Boxplots of fare by passenger class.
- A correlation heatmap.

## Note
Ensure you have the Titanic dataset (`train.csv`) in the correct directory before running the script.

## License
This project is for educational purposes and uses publicly available datasets.
