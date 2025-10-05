# Part 1 - Data and Dataframes

[Next Part: Plotting and Graphing](https://github.com/Bonky00/starting-Python/blob/main/Section%202%20-%20Processing%20Data/Part%202%20-%20Plotting%20and%20Graphing.md)

[Example Code Folder](https://github.com/Bonky00/starting-Python/tree/main/Section%202%20-%20Processing%20Data/example_code)

---

## Overview

A very common way to access and manipulate data is through a Python package named `pandas` and creating what is known as a `DataFrame`.

`DataFrames` make manipulation of many different source files relatively easy, allowing for unification of structure and enabling operations to be conducted on them. This will be demonstrated later in this section. Common files to be parsed into a `DataFrame` are (but not limited to by any means):

- text (.txt)
- csv (.csv)
- excel (.xlsx)

Examples of a .txt file and a .csv file are found in the `example_code` folder:

- [Text File](./example_code/random_data.txt)
- [CSV File](./example_code/random_data.csv)

These files were created with random values using the supplied [Python file](./example_code/generate_rand_data.py); created to have two columns of data to plot as an example.

## Step 2 - Processing the Data

### Loading the data

The first step of processing the data file is to have the data read into the Python script in a way that it will be able to understand and handle the information.

For this, we will use the package `pandas`, which is a standard package for handling various forms of data structures and converting them into what is known as a `DataFrame` or `df` for short.

To import `pandas` we will put the following line at the top of the script:

```python
import pandas as pd
```

- This will import the `pandas `package, with the 'nickname' of `pd` (so we don't have to type out the full word each time we want to use it.)

To load the data into a dataframe, we can use use the following line to create a vaiables called `df_text` and `df_csv`, and assign the data from their respective files into the a `DataFrame`format.

```python
import os # We'll need this to handle file paths correctly

# Get the directory where the current script is located
script_dir = os.path.dirname(__file__)

# Load the data. Pandas will automatically detect the header row (expected to be 'x' and 'y').
# For the .txt file, we explicitly tell pandas that values are separated by tabs (delimiter="\t").
# The files are expected to be in the SAME directory as this Python script.
df_text = pd.read_csv(os.path.join(script_dir, "random_data.txt"), delimiter="\t")
df_csv = pd.read_csv(os.path.join(script_dir, "random_data.csv"))

print("This is the first lines of the text based dataframe:")
print(df_text.head()) #the .head() function allows us to only see the first few lines of the dataframe

print("\nThis is the first lines of the csv based dataframe:")
print(df_csv.head()) #the .head() function allows us to only see the first few lines of the dataframe
```

Important Notes:

- Your `random_data.txt` and `random_data.csv` files are expected to contain header rows named '`x`' and '`y`'. pandas will automatically detect and use these as column names.
- For the `.txt` file, we've added `delimiter="\t`" because text files often use tabs instead of commas to separate values. This ensures `pandas` reads the columns correctly.
- The `import os` and `os.path.join(script_dir, ...)` are crucial for the script to find your data files reliably, as they are now expected to be in the same directory as the Python script itself.

### Plotting the dataframe

Having the data is great, but seeing the data is better.
This seciton we will be plotting the data from the two files useing another extremely common package called `matplotlib`.

`Matplotlib` allows you to make very simple, to extremely complex plots (depending how much you want to control yourself.). We will change some of the plot settings in this example, but note that EVERY aspect of the plot can be altered, but the defualts are a great starting point.

To begin, we much import the `matplotlib` package using the following line:

```python
import matplotlib.pyplot as plt
```

Next we will be use the pacakage to graph the date as two scatter plots. The code to do this is below, with teh explaination of the parts following the code:

```python
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

# Save the plots to a file
plt.savefig(os.path.join(script_dir, "data_visualization.png"))

#Open the plot in a window for viewing
plt.show()
```

- `fig, axes = plt.subplots(1, 2, figsize=(12, 5))` is telling the program to create a figure with subplots arranged with 1 row and two columns with an overall figure size of 12in x 5in.

- `axes[0].scatter(df_text["x"], df_text["y"], color="blue", alpha=0.7)` takes the first axes or subplot, and is creating a scatter plot in that area. The data used for the scatter plot are columns named '`x`' and '`y`' from the `df_text` dataframe (which pandas automatically read from your file's header). We also set the color to blue, with a transparency of 70%.

- The rest of the lines for `axes[0]` are more formatting specifics (title, labels, grid).

- The plot for the second scatter plot is created in the same way, only using `axes[1]` to plot it on the second subplot.

- `plt.tight_layout()` is used to ensure that the axes and alignment are formatted correctly without overlapping.

- `plt.savefig(os.path.join(script_dir, "data_visualization.png"))` is the function that will save the generated plot as an image file named data_visualization.png in the same directory as your Python script.

### Putting it Together

Now that we have the theory and the code snippets, let's put it all together and run it.

1.  **Create a New Python File:**

    - In your VS Code environment, create a new file named data_processing_example.py (or any other descriptive name).
    - Crucially, ensure your `random_data.txt` and `random_data.csv` files are placed in the same directory as this `data_processing_example.py` script.

2.  **Copy and Paste the Code:**

    - Paste the entire Python script below into your newly created `data_processing_example.py` file.

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import os  # Import the os module for path manipulation

    # Get the directory where the current script is located
    script_dir = os.path.dirname(__file__)

    # Load the data, making sure to specify the full path to the data files
    # The .txt file is read with a tab delimiter.
    # The files are expected to be in the SAME directory as this Python script.
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

    # Save the plots to a file
    plt.savefig(os.path.join(script_dir, "data_visualization.png"))

    #Open the plot in a window for viewing
    plt.show()
    ```

3.  Install Dependencies (if not already done):

    - If you haven't already, install the necessary packages within your active virtual environment `(.venv)`. This ensures pandas and `matplotlib` are available in your isolated environment.

4.  **Run the Script:**

    - In your VS Code terminal (with the virtual environment (`.venv`) activated), navigate to the directory where you saved `data_processing_example.py`.
    - Run the script using the command:
      ```bash
      python data_processing_example.py
      ```
    - Alternatively, you can click the "Run Python File" button in the top right corner of VS Code while `data_processing_example.py` is open. VS Code should automatically use the selected Python interpreter from your `.venv`.

5.  **Observe the Output:**

    - **Terminal Output:** You will first see the `print` statements showing the head (first 5 rows by default) of both `df_text` and `df_csv` DataFrames. This confirms that `pandas` successfully read your data files.

      ```text
      This is the first lines of the text based dataframe:
          Column1  Column2
      0    29.74    72.58
      1    82.72    62.83
      2    44.40    30.63
      3    45.50    75.83
      4    29.80    17.65

      This is the first lines of the csv based dataframe:
          Column1  Column2
      0    39.46    84.77
      1    56.77    11.13
      2    99.27    56.32
      3    13.31    20.30
      4    53.86    78.02
      ```

      (Note: Your actual numbers will be different as they are randomly generated.)

    - **Plot Window:** A new window will appear displaying two scatter plots side-by-side. The left plot will show the data from `random_data.txt` (in blue), and the right plot will show the data from `random_data.csv` (in red). This visualization helps you quickly understand the distribution and relationship of the 'Column1' and 'Column2' values in each dataset.
    - **Image File Output:** A new image file named `data_visualization.png `will be created in the same directory as your `data_processing_example.py` script. Open this image file to view the two scatter plots side-by-side.

---

[Next Part: Plotting and Graphing](https://github.com/Bonky00/starting-Python/blob/main/Section%202%20-%20Processing%20Data/Part%202%20-%20Plotting%20and%20Graphing.md)

[Example Code Folder](https://github.com/Bonky00/starting-Python/tree/main/Section%202%20-%20Processing%20Data/example_code)

---
