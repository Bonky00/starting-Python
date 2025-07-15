import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os  # For saving the plot to a specific path

# --- Data Generation ---
x_data = np.random.rand(100) * 100
y_data = np.random.randn(100) * 20 + 50

data_df = pd.DataFrame({"X_Value": x_data, "Y_Value": y_data})

print("First 5 rows of generated data:")
print(data_df.head())

# --- Plotting ---
# Create a single figure and an axes object for our plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the generated data as a scatter plot
ax.scatter(
    data_df["X_Value"],
    data_df["Y_Value"],
    color="green",
    alpha=0.6,
    label="Random Data Points",
)

# Add a title and labels to the plot
ax.set_title("Scatter Plot of Generated Random Data")
ax.set_xlabel("X Value (0-100)")
ax.set_ylabel("Y Value (Centered at 50)")

# Add a grid for better readability
ax.grid(True, linestyle="--", alpha=0.7)

# Add a legend to explain what the points represent
ax.legend()

# Ensure layout is tight to prevent labels from overlapping
plt.tight_layout()

# Define the path to save the plot (in the same directory as the script)
script_dir = os.path.dirname(__file__)
output_file_path = os.path.join(script_dir, "generated_data_plot.png")

# Save the plot to a file
plt.savefig(output_file_path)

print(f"\nPlot saved to: {output_file_path}")
