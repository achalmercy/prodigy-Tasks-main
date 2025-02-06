# Social Media Sentiment Analysis and Visualization

This project analyzes sentiment data from Twitter datasets and generates word clouds for different sentiment labels. It combines sentiment columns into a single column representing the most significant sentiment and visualizes sentiment distribution and word clouds.

## Features:
- Load and combine training and validation datasets.
- Clean and preprocess text data (removes URLs, special characters, and stopwords).
- Analyze sentiment using predefined sentiment columns (`Positive`, `Negative`, `Neutral`, `Irrelevant`).
- Generate word clouds for each sentiment label.
- Output analysis results (e.g., sentiment distribution, sentiment value counts) to a text file (`output.txt`).

## Requirements

- Python 3.x
- Required Python libraries:
  - pandas
  - matplotlib
  - wordcloud
  - nltk
  - seaborn

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib wordcloud nltk seaborn
