import pandas as pd  # We still need pandas to work with DataFrames

# Define the path to our CSV file.
# Since 'sample_data.csv' is in the same folder as 'read_csv.py',
# we just need its name.
file_path = "sample_data.csv"

try:
    # Read the CSV file into a Pandas DataFrame
    df_from_csv = pd.read_csv(file_path)

    print(f"Successfully loaded data from '{file_path}':")
    print(df_from_csv)

    # You can now work with this DataFrame just like before!
    print("\nPeople from New York:")
    print(df_from_csv[df_from_csv["City"] == "New York"])

except FileNotFoundError:
    print(
        f"Error: The file '{file_path}' was not found. Make sure it's in the same folder as your script."
    )
except Exception as e:
    print(f"An error occurred: {e}")
