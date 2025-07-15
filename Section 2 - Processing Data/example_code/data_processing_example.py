import pandas as pd
import matplotlib.pyplot as plt
import os  # Import the os module for path manipulation

# Get the directory where the current script is located
script_dir = os.path.dirname(__file__)

# Load the data, making sure to specify the full path to the data files
df_text = pd.read_csv(os.path.join(script_dir, "random_data.txt"), delimiter="\t")
df_csv = pd.read_csv(os.path.join(script_dir, "random_data.csv"))

print("This is the first lines of the text based dataframe:")
print(df_text.head())

print("\nThis is the first lines of the csv based dataframe:")
print(df_csv.head())

# Create a figure and a set of subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot df_text data using the detected column names 'x' and 'y'
axes[0].scatter(df_text["x"], df_text["y"], color="blue", alpha=0.7)
axes[0].set_title("Random Data from TXT File")
axes[0].set_xlabel("X Value")  # Consistent with 'x' column
axes[0].set_ylabel("Y Value")  # Consistent with 'y' column
axes[0].grid(True, linestyle="--", alpha=0.6)

# Plot df_csv data using the detected column names 'x' and 'y'
axes[1].scatter(df_csv["x"], df_csv["y"], color="red", alpha=0.7)
axes[1].set_title("Random Data from CSV File")
axes[1].set_xlabel("X Value")  # Consistent with 'x' column
axes[1].set_ylabel("Y Value")  # Consistent with 'y' column
axes[1].grid(True, linestyle="--", alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
# plt.show()
plt.savefig("data_visualization.png")
