Now that your workspace is set up and your virtual environment is active, it's time to write some Python code! We'll start with a classic "Hello, World!" and then quickly move on to a simple data example using powerful Python libraries.

### Step 1: Your Very First Python Script - "Hello, World!"

This is the traditional first program for learning any new language. It just prints a message to the screen.

1. **Open `hello_world.py`:** If you closed it, open the `hello_world.py` file you created in the previous section by clicking on it in the VS Code Explorer.    
2. **Write the Code:** In the empty `hello_world.py` file, type the following line of code exactly as it appears:
```python
print("Hello, World!")
```
- `print()` is a built-in Python function that displays whatever you put inside the parentheses to the console.    
- The text inside the parentheses, enclosed in double quotes (`""`), is called a "string" (a sequence of characters).

3. **Save Your File:** Go to **File > Save** (or press `Ctrl + S`).   
4. **Run Your Script:**   
	- **Option 1: Click Run Python File at the top of the file.** 

	![Pasted image 20250703012026](https://github.com/user-attachments/assets/2003b663-5023-4ac9-9731-e90721958417)

	-  **Option 2: Open the Integrated Terminal:** If your terminal is not open, go to **Terminal > New Terminal**. Make sure your virtual environment `(venv)` is active at the beginning of the prompt.
    ![Pasted image 20250703010941](https://github.com/user-attachments/assets/4b0e03f5-5e5f-4293-89d3-ee2a999ea107)



### Step 2: Working with Data - Introducing Pandas DataFrames

Now, let's dive into data. In Python, especially for data analysis, a library called **Pandas** is incredibly popular. It provides a data structure called a **DataFrame**, which is like a super-powered spreadsheet or a table in a database.

First, we need to install the Pandas library into our virtual environment.

1. **Install Pandas:** In your VS Code integrated terminal (make sure `(venv)` is still active), type the following command and press Enter: **`pip install pandas`**
	-  `pip` is Python's package installer. It's how you download and install external
	- You'll see some progress messages as `pip` downloads and installs Pandas and its dependencies.

2. **Create a New Python File:** In your VS Code Explorer, create a new file in your `my_first_python_project` folder and name it `simple_data.py`.
    
**Write the Data Code:** In `simple_data.py`, type the following code:
import pandas as pd # This line imports the pandas library
```python


import pandas as pd # This line imports the pandas library

# Create some sample data as a Python dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Print the entire DataFrame
print("Our first DataFrame:")
print(df)

# Print a specific column (Series)
print("\nOnly the 'Name' column:")
print(df['Name'])

# Print rows where Age is greater than 25
print("\nPeople older than 25:")
print(df[df['Age'] > 25])

```
- **Save Your File:** Save `simple_data.py`.    
- **Run Your Script:**: In the same way you ran 'hello_world.py'

**What you'll see:** The output will show your data nicely formatted as a table, then just the names, and finally only the rows for Bob and David. This shows how easy it is to create, view, and filter data with DataFrames!
![Pasted image 20250703012059](https://github.com/user-attachments/assets/429605a6-b14d-41fb-9e50-528dbb5ab531)



### Step 3: Visualizing Data - Introducing Matplotlib

Seeing numbers is one thing, but seeing them visually can tell a much clearer story. **Matplotlib** is a widely used Python library for creating static, animated, and interactive visualizations.

First, we need to install Matplotlib into our virtual environment.

1. **Install Matplotlib:** In your VS Code integrated terminal (make sure `(venv)` is still active), type the following command and press Enter: **` pip install matplotlib`**
	- Similar to Pandas, `pip` will download and install Matplotlib.
2. **Create a New Python File:** In your VS Code Explorer, create a new file in your `my_first_python_project` folder and name it `data_plot.py`.    
3. **Write the Plotting Code:** In `data_plot.py`, type the following code. We'll reuse our Pandas DataFrame data for this.
```python
import pandas as pd
import matplotlib.pyplot as plt # This imports the plotting module

# Create the same sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# --- Let's create a simple bar chart of Ages ---
plt.figure(figsize=(8, 5)) # Create a figure (the overall window for the plot)
plt.bar(df['Name'], df['Age'], color='skyblue') # Create a bar chart: Names on X, Ages on Y

plt.xlabel('Person') # Label for the horizontal axis
plt.ylabel('Age')    # Label for the vertical axis
plt.title('Ages of Our Friends') # Title of the plot
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a light grid for readability

plt.show() # Display the plot! This command is essential to make the plot appear

# --- Let's create a scatter plot of Age vs. a hypothetical 'Score' ---
# (Let's add a 'Score' column to our DataFrame for this example)
df['Score'] = [85, 92, 78, 95]

plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Score'], color='red', s=100, alpha=0.8, edgecolors='black') # s is size of points
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Age vs. Score for Our Friends')
plt.grid(True) # Add a grid
plt.savefig("example image.png") #This will save the image in the  working folder!
plt.show() # Display this plot too!

```

### Step 4: Reading Data from a File - CSV to DataFrame

Most of the time, your data won't be typed directly into your script. It will come from files! A very common format for tabular data (like spreadsheets) is a **CSV** (Comma Separated Values) file.

Let's learn how to read a CSV file directly into a Pandas DataFrame.

1. **Create a Sample CSV File:** Before we can read a CSV, we need one! In your `my_first_python_project` folder in VS Code, create a **new file** and name it `sample_data.csv`.

    Now, copy and paste the following text exactly into `sample_data.csv`:
    ```
    Name,Age,City,Occupation
    Alice,24,New York,Engineer
    Bob,27,Los Angeles,Designer
    Charlie,22,Chicago,Student
    David,32,Houston,Doctor
    Eve,29,Miami,Artist
    ```
- **What is a CSV?** It's a plain text file where each line is a row of data, and values within each row are separated by commas. The first line usually contains the column headers.    
- **Save Your File:** Make sure to save `sample_data.csv`.

2. **Create a New Python File for Reading CSV:** In your VS Code Explorer, create another new file in your `my_first_python_project` folder and name it `read_csv.py`.
3. **Write the CSV Reading Code:** In `read_csv.py`, type the following code:
```python
import pandas as pd # We still need pandas to work with DataFrames

# Define the path to our CSV file.
# Since 'sample_data.csv' is in the same folder as 'read_csv.py',
# we just need its name.
file_path = 'sample_data.csv'

try:
    # Read the CSV file into a Pandas DataFrame
    df_from_csv = pd.read_csv(file_path)

    print(f"Successfully loaded data from '{file_path}':")
    print(df_from_csv)

    # You can now work with this DataFrame just like before!
    print("\nPeople from New York:")
    print(df_from_csv[df_from_csv['City'] == 'New York'])

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Make sure it's in the same folder as your script.")
except Exception as e:
    print(f"An error occurred: {e}")
```
- `pd.read_csv()` is a powerful Pandas function that reads data from a CSV file and automatically turns it into a DataFrame.    
- We've added a `try...except` block. This is a good programming practice to gracefully handle potential errors, like if the file isn't found.
4. **Save your file**
5. **Run the script**
![Pasted image 20250703013835](https://github.com/user-attachments/assets/7858e43c-dc53-43cd-b061-3c579f67250e)

