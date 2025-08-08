# The code

In this section we will go through creating each part of the code step-by-step and build up the whole script as we go along.

## The data

With the data downloaded, we need to have the computer look at the data and save itin a way that it can manipulate it. To do this we will use python to:

- open a file menu to select the files.
- remember the names and paths of all selcted files
- use the file paths to iterativly open each file and load the data into a dataframe

This task requires a couple of new libraries:

- `tkinter`: A standard Python library for creating graphical user interfaces. We'll use its `filedialog` module to open a native file selection window.

- `pandas`: The data processing library we've used before.

Here is the complete script. We'll break it down step-by-step below. The python file can be found in the [example code folder](/Section%203%20-%20Putting%20it%20together/Example_code/) ([select_files.py](/Section%203%20-%20Putting%20it%20together/Example_code/select_files.py)).

```python
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

else:
    print("No files were selected. Exiting script.")

```

The resulting dataframe will have a first few rows that look like this:

| data_1.csv_col1 | data_1.csv_col2 | data_2.csv_col1 | data_2.csv_col2 | data_3.csv_col1 | data_3.csv_col2 |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| 1               | 54              | 1               | 39              | 1               | 57              |
| 2               | 62              | 2               | 49              | 2               | 45              |
| 3               | 62              | 3               | 66              | 3               | 28              |
| 4               | 57              | 4               | 18              | 4               | 58              |
| 5               | 53              | 5               | 52              | 5               | 22              |

## Processing the data

Now that the data is collected into a dataframe, we can look closer at the structure and decide how to approach the rest of the tasks.

Notice that the table is has an index column on the left. This can be used to graph the values easily. Alternativly we could use each data set's ID column (now labeled as \_col1 i nthe dataframe) with its corresponding values.

Depending on the problem, and the data envolved, how you approach it will change. Things to consider:

- are each of the datasets indexed the same
- are all of the data points of the same type (float, int, datetime, etc.)
- are there missing values
- are the columns the same length (creating missing vlaues in the combined dataframe)

For this example we will use each of the date set's _"\_col1"_ ID as the x-axis and it's corrisponding _"\_col2"_ value as the y-axis for simplicity.

### Extracting the stats from the data

We will add the following code to the end of the previous script to calulate the

- min
- max
- mean

of each of the datasets and print them i nthe terminal.

```python
# len(combined_df.columns) gives us the total number of columns
total_columns = len(combined_df.columns)

# We loop from index 1 (the second col) to the end, in steps of 2
for i in range(1, total_columns, 2):
    # Get the column name using the index
    column_name = combined_df.columns[i]

    #calulate the stats. pandas has builtin functions to do this
    col_min = combined_df[column_name].min()
    col_max = combined_df[column_name].max()
    col_mean = combined_df[column_name].mean()

    # print out the information
    print(f"The minimum value of {column_name} is: \t\t{col_min}")
    print(f"The maximum value of {column_name} is: \t\t{col_max}")
    print(f"The average value of {column_name} is: \t\t{col_mean}")


```

This code has been updated into the previous file and can be found at [extract_stats.py](/Section%203%20-%20Putting%20it%20together/Example_code/extract_stats.py)

### Plotting the columns

tbd
