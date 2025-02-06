import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import seaborn as sns

# Step 1: Load and Combine Datasets
def load_data(train_file, validation_file):
    train_data = pd.read_csv(train_file)
    val_data = pd.read_csv(validation_file)
    combined_data = pd.concat([train_data, val_data], ignore_index=True)
    return combined_data

# Step 2: Data Cleaning
def clean_text(text):
    import re
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Step 3: Generate Word Cloud
def generate_wordcloud(data, sentiment_label):
    text = " ".join(data[data['sentiment'] == sentiment_label]['text'].apply(clean_text))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for {sentiment_label.capitalize()} Sentiment")
    plt.show()

# Step 4: Sentiment Distribution Visualization
def plot_sentiment_distribution(data):
    sns.countplot(x='sentiment', data=data, palette='viridis')
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

# Step 5: Main Function
def main():
    # Open the output file in write mode
    with open('output.txt', 'w', encoding='utf-8') as f:
        # Update file paths
        train_file = "twitter_training.csv"
        validation_file = "twitter_validation.csv"

        # Load data
        data = load_data(train_file, validation_file)

        # Check if the data loaded correctly
        if data.empty:
            f.write("Error: Data is empty.\n")
            return

        # Inspect column names
        f.write("Column Names:\n")
        f.write(str(data.columns) + "\n")

        # Inspect first few rows
        f.write("Data Overview:\n")
        f.write(str(data.head()) + "\n")

        # Define sentiment columns
        sentiment_columns = ['Positive', 'Negative', 'Neutral', 'Irrelevant']

        # Check if all sentiment columns exist in the dataset
        missing_columns = [col for col in sentiment_columns if col not in data.columns]
        if missing_columns:
            f.write(f"Missing sentiment columns: {missing_columns}\n")
            return

        # Combine sentiment columns if all exist
        try:
            data['sentiment'] = data[sentiment_columns].idxmax(axis=1)
        except Exception as e:
            f.write(f"Error combining sentiment columns: {e}\n")
            return

        # Write the value counts of the sentiment column
        f.write("Sentiment Value Counts:\n")
        f.write(str(data['sentiment'].value_counts()) + "\n")

        # Plot sentiment distribution
        plot_sentiment_distribution(data)

        # Generate word clouds for each sentiment
        for sentiment in data['sentiment'].unique():
            f.write(f"Generating word cloud for sentiment: {sentiment}\n")
            generate_wordcloud(data, sentiment)

if __name__ == "__main__":
    main()
