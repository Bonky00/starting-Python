# Import necessary libraries
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Create a hidden Tkinter window
# This is a bit of a trick to use the file dialog without having a full window show up
root = tk.Tk()
root.withdraw()

# Open a file selection dialog to allow the user to select multiple files.
# The `filetypes` parameter helps filter for specific file types.
print("Please select one or more data files...")
file_paths = filedialog.askopenfilenames(
    title="Select Data Files", filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
)

# --- Process the selected files ---
combined_df = pd.DataFrame()  # Initialize an empty DataFrame to hold combined data

# Check if the user selected any files
if file_paths:

    # Loop through each file path that was selected
    for file_path in file_paths:

        try:
            # Get just the filename for a clean printout
            file_name = os.path.basename(file_path)
            print(f"Loading data from {file_name}...")

            # Use pandas to read the data from the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Take the first two columns of the DataFrame and add them to the combined DataFrame
            combined_df[f"{file_name}_col1"] = df.iloc[:, 0]
            combined_df[f"{file_name}_col2"] = df.iloc[:, 1]

        except Exception as e:
            print(f"Error loading {file_name}: {e}")

    print("Done! The first 5 rows of the combined data are:")
    print(combined_df.head())
    print("\n")


else:
    print("No files were selected. Exiting script.")
# len(combined_df.columns) gives us the total number of columns
total_columns = len(combined_df.columns)

# We loop from index 1 (the second col) to the end, in steps of 2
for i in range(1, total_columns, 2):
    # Get the column name using the index
    column_name = combined_df.columns[i]

    # calulate the stats. pandas has builtin functions to do this
    col_min = combined_df[column_name].min()
    col_max = combined_df[column_name].max()
    col_mean = combined_df[column_name].mean()

    # print out the information
    print(f"The minimum value of {column_name} is:   {col_min}")
    print(f"The maximum value of {column_name} is:   {col_max}")
    print(f"The average value of {column_name} is:   {col_mean}\n")
