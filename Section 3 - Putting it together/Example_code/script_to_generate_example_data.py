import csv
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
folder_location = "Section 3 - Putting it together/Example_data/"
file_name = "data_3.csv"


file_name = f"{folder_location}{file_name}"
num_rows = 1000
mean = 50  # The center of the bell curve
std_dev = 15  # The "spread" of the data
column_headers = ["ID", "Value"]

# --- GENERATE DATA ---
# Use numpy.random.normal() to create an array of data with a normal distribution.
# We cast it to int as we don't need floats, and the distribution is still valid.
data_values = np.random.normal(loc=mean, scale=std_dev, size=num_rows).astype(int)
id_values = np.arange(1, num_rows + 1)

# --- WRITE TO CSV ---
with open(file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_headers)

    for i in range(num_rows):
        writer.writerow([id_values[i], data_values[i]])

print(f"Successfully generated '{file_name}' with {num_rows} rows.")
"""
# --- VISUALIZE THE DISTRIBUTION ---
plt.figure(figsize=(8, 6))
plt.hist(data_values, bins=30, edgecolor="black", alpha=0.7)
plt.title("Histogram of Generated Normal Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
"""
