import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
train = pd.read_csv('train.csv')

def data_cleaning_and_eda(df):
    """Perform data cleaning and exploratory data analysis."""
    print("Initial Dataset Info:\n")
    print(df.info())

    print("\nDataset Description:\n")
    print(df.describe(include='all'))

    print("\nChecking for Missing Values:\n")
    print(df.isnull().sum())

    # Fill missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill Age with median
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill Embarked with mode

    # Drop unnecessary columns (e.g., 'Cabin' due to high missing values, 'Name' for simplicity)
    df.drop(columns=['Cabin', 'Name', 'Ticket'], inplace=True)

    print("\nAfter Cleaning:\n")
    print(df.isnull().sum())

    # Exploratory Data Analysis
    print("\nSurvival Distribution:")
    print(df['Survived'].value_counts())

    sns.countplot(data=df, x='Survived')
    plt.title('Survival Count')
    plt.show()

    sns.countplot(data=df, x='Pclass', hue='Survived')
    plt.title('Survival by Passenger Class')
    plt.show()

    sns.histplot(df['Age'], kde=True, hue=df['Survived'])
    plt.title('Age Distribution with Survival')
    plt.show()

    sns.boxplot(data=df, x='Pclass', y='Fare')
    plt.title('Fare Distribution by Passenger Class')
    plt.show()

    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    print("\nInsights:\n")
    print("1. Majority of passengers did not survive.")
    print("2. Higher survival rates for passengers in 1st class.")
    print("3. Children (lower Age) have slightly higher survival rates.")
    print("4. Fare is correlated with class and survival.")

# Run the function
data_cleaning_and_eda(train)
