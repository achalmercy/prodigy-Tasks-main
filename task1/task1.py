# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data (update the file path as needed)
file_path = "/python/prodigy/API_SP.POP.TOTL_DS2_en_csv_v2_900.csv"  # Replace with your file path
data = pd.read_csv(file_path, skiprows=4)

# Filter data for a specific year (2023) and clean it
population_2023 = data[["Country Name", "2023"]].dropna()
population_2023["2023"] = population_2023["2023"].astype(float)

# Plot the histogram
plt.figure(figsize=(12, 6))
plt.hist(population_2023["2023"], bins=30, color='skyblue', edgecolor='black')
plt.title("Population Distribution in 2023", fontsize=16)
plt.xlabel("Population", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
