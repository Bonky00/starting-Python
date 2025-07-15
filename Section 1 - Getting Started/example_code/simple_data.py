import pandas as pd  # This line imports the pandas library

# Create some sample data as a Python dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Print the entire DataFrame
print("Our first DataFrame:")
print(df)

# Print a specific column (Series)
print("\nOnly the 'Name' column:")
print(df["Name"])

# Print rows where Age is greater than 25
print("\nPeople older than 25:")
print(df[df["Age"] > 25])
