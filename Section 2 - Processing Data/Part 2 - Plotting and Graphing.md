# Part 2 - Plotting and Graphing

In this part, we will scratch the surface on using `matplotlib` to present data, using some of its most common features.

We will use the following lines of code at the beginning of the script to generate random data each time the script is run. This ensures that every time you execute the script, you'll see a slightly different distribution in the plots, making it a good way to demonstrate plotting without relying on external data files for this section.

To generate random data efficiently, we'll use another powerful Python library: `numpy` (Numerical Python). `numpy` is fundamental for numerical computing in Python and is often used alongside pandas and matplotlib.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data
# np.random.rand(100) generates 100 random numbers between 0 and 1
# We multiply by 100 to get values between 0 and 100
# np.random.randn(100) generates 100 random numbers from a standard normal distribution (mean 0, variance 1)
# We multiply by 20 and add 50 to get a distribution roughly centered around 50

x_data = np.random.rand(100) * 100
y_data = np.random.randn(100) * 20 + 50

# Combine the generated data into a pandas DataFrame
# This is a good practice as DataFrames are very convenient for plotting
data_df = pd.DataFrame({
    'X_Value': x_data,
    'Y_Value': y_data
})

# Display the first few rows of our generated data
print("First 5 rows of generated data:")
print(data_df.head())

# Now we are ready to plot data_df!
```

### Explanation of the Data Generation Code:

- `import numpy as np:` This line imports the `numpy` library, giving it the common alias `np`.
- `x_data = np.random.rand(100) * 100`:

  - `np.random.rand(100)` creates an array of 100 random floating-point numbers, uniformly distributed between 0.0 and 1.0.

  - Multiplying by `100` scales these numbers to be between 0.0 and 100.0. This could represent a general quantity or score.

- `y_data = np.random.randn(100) * 20 + 50:
` - `np.random.randn(100)` creates an array of 100 random floating-point numbers drawn from a "standard normal" (Gaussian) distribution (mean 0, variance 1).

          - Multiplying by `20` scales the standard deviation, making the spread wider.

          - Adding `50` shifts the mean of the distribution to around `50`. This kind of data often represents measurements with some natural variation around an average.

- `data_df = pd.DataFrame({'X_Value': x_data, 'Y_Value': y_data})`: We then take these two `numpy` arrays (`x_data and y_data`) and put them into a `pandas` `DataFrame`. This is excellent practice because `DataFrames` offer easy ways to label columns ('`X_Value`', '`Y_Value`') and provide convenient methods that integrate well with matplotlib.

- p`rint(data_df.head())`: Just like in Part 1, we use `.head()` to quickly inspect the first few rows of our newly created DataFrame, ensuring the data looks as expected.

Now that we have our `data_df` with generated '`X_Value`' and '`Y_Value`' columns, we can proceed to plot them using matplotlib.

## Creating Your First Plot

Now that we have our `data_df` with generated '`X_Value`' and '`Y_Value`' columns, let's create a basic scatter plot to visualize this data. This will be a single plot within our figure.

```python
# Create a single figure and an axes object for our plot
fig, ax = plt.subplots(figsize=(8, 6)) # A single plot (no multiple rows/cols needed here)

# Plot the generated data as a scatter plot
ax.scatter(data_df['X_Value'], data_df['Y_Value'], color='green', alpha=0.6, label='Random Data Points')

# Add a title and labels to the plot
ax.set_title('Scatter Plot of Generated Random Data')
ax.set_xlabel('X Value (0-100)')
ax.set_ylabel('Y Value (Centered at 50)')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend to explain what the points represent (useful when plotting multiple datasets)
ax.legend()

# Ensure layout is tight to prevent labels from overlapping
plt.tight_layout()

# Define the path to save the plot (in the same directory as the script)
script_dir = os.path.dirname(__file__)
output_file_path = os.path.join(script_dir, 'generated_data_plot.png')

# Save the plot to a file
plt.savefig(output_file_path)

print(f"\nPlot saved to: {output_file_path}")
```

Explanation of the Plotting Code:

- `fig, ax = plt.subplots(figsize=(8, 6))`:

  - This creates a figure (f`ig`) and a single set of axes (`ax`) for our plot. Unlike Part 1 where we had axes (plural) for multiple subplots, ax (singular) is used here for a single plot.

  - `figsize=(8, 6)` sets the dimensions of the overall figure to 8 inches wide by 6 inches tall.

- `ax.scatter(data_df['X_Value'], data_df['Y_Value'], ...)`:

  - This is the core command to create a scatter plot on our ax (axes object).

  - d`ata_df['X_Value'] `provides the data for the x-axis, directly from our DataFrame.

  - `data_df['Y_Value']` provides the data for the y-axis.

  - `color='green'`: Sets the color of the scatter points to green.

  - `alpha=0.6`: Makes the points slightly transparent (60% opaque), which can be useful for visualizing overlapping points.

  - `label='Random Data Points'`: Assigns a label to this series of points. This label will be used if a legend is displayed.

- `ax.set_title(...)`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)`: These methods are used to add a descriptive title and labels for the X and Y axes, making your plot understandable.

- `ax.grid(True, linestyle='--', alpha=0.7)`: Adds a grid to the plot, improving readability. l`inestyle='--'` makes the grid lines dashed, and `alpha=0.7` makes them semi-transparent.

- `ax.legend()`: This command displays a legend on the plot, using the label we provided in the scatter function ('Random Data Points'). Legends are essential when you have multiple data series on one plot.

- `plt.tight_layout()`: Automatically adjusts plot parameters for a tight layout, preventing labels from overlapping.

- `script_dir = os.path.dirname(__file__)` and `output_file_path = os.path.join(script_dir, 'generated_data_plot.png')`: These lines use the os module (which you are already familiar with) to construct a robust file path for saving your plot. The plot will be saved in the same directory as your Python script.

- `plt.savefig(output_file_path)`: This command saves the figure to the specified file path.

## Putting it together

Let's consolidate all the code for this section into a single script and run it.

1. **Create a New Python File**:

   - In your VS Code environment, create a new file named `part2_plotting_example.py` in the root of your project directory. This script will generate its own data, so it doesn't need to be in the `example_code` subfolder for this specific part, though you can place it there if you prefer to keep all examples together.

2. **Copy and Paste the Code**:

   - Paste the entire Python script below into your newly created `part2_plotting_example.py` file.

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os # For saving the plot to a specific path

# --- Data Generation ---
x_data = np.random.rand(100) * 100
y_data = np.random.randn(100) * 20 + 50

data_df = pd.DataFrame({
    'X_Value': x_data,
    'Y_Value': y_data
})

print("First 5 rows of generated data:")
print(data_df.head())

# --- Plotting ---
# Create a single figure and an axes object for our plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the generated data as a scatter plot
ax.scatter(data_df['X_Value'], data_df['Y_Value'], color='green', alpha=0.6, label='Random Data Points')

# Add a title and labels to the plot
ax.set_title('Scatter Plot of Generated Random Data')
ax.set_xlabel('X Value (0-100)')
ax.set_ylabel('Y Value (Centered at 50)')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a legend to explain what the points represent
ax.legend()

# Ensure layout is tight to prevent labels from overlapping
plt.tight_layout()

# Define the path to save the plot (in the same directory as the script)
script_dir = os.path.dirname(__file__)
output_file_path = os.path.join(script_dir, 'generated_data_plot.png')

# Save the plot to a file
plt.savefig(output_file_path)

print(f"\nPlot saved to: {output_file_path}")
```

Change some of the script and re-run it. Play arouns with colors and formatting.

**_Here are the matplotlib example pages_**: [Matplotlib Example Website Link](https://matplotlib.org/stable/gallery/index.html)
