# Traffic Accident Data Analysis

## Overview
This project analyzes traffic accident data to identify patterns and visualize contributing factors like deaths over years and the relationship between historical population and accident-related fatalities. It dynamically handles missing data and performs analysis based on the available columns in the dataset.

## Features
- **Dynamic Column Handling**: The script adjusts to the dataset's structure and analyzes only available data.
- **Trend Analysis**: Visualizes the trend of deaths over the years.
- **Correlation Exploration**: Explores the relationship between historical population and fatalities.
- **Data Preprocessing**: Handles missing values gracefully.

## Requirements
- Python 3.7+
- Required Python libraries:
  - pandas
  - matplotlib
  - seaborn

Install the required libraries using pip:
```bash
pip install pandas matplotlib seaborn
```

## Dataset
The dataset should be in CSV format and contain at least some of the following columns:
- `Year`: The year of the accident data.
- `Deaths`: Number of deaths caused by accidents.
- `Historical_Population`: Historical population data.

Ensure the file is correctly formatted before running the script.

## Usage
1. Place your dataset file in the project directory (e.g., `output.csv`).
2. Update the `file_path` variable in the script with the dataset's path.
3. Run the script:
   ```bash
   python main.py
   ```

## Output
- **Trend Analysis**: A line plot showing deaths over the years.
- **Correlation Exploration**: A scatter plot visualizing the relationship between historical population and deaths.
- If columns like `Road_Condition`, `Weather`, `Time`, `Latitude`, and `Longitude` are present in your dataset, further analyses and visualizations can be added.

## Example Output
### Deaths Over Years
A line chart showing the trend of accident-related deaths across different years.

### Historical Population vs. Deaths
A scatter plot exploring how historical population correlates with accident fatalities.

## Notes
- If the dataset lacks the required columns, the script will skip the analysis and provide appropriate messages.
- The script generates clear and actionable plots for visualization.

## License
This project is licensed under the MIT License.
