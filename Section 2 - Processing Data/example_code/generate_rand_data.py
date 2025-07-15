import numpy as np
import pandas as pd


def generate_and_save_random_data(num_rows):
    """
    Generates random data for 'x' and 'y' columns and saves it as CSV and TXT
    in the same directory where the script is executed.

    Args:
        num_rows (int): The number of data points (rows) to generate.
    """

    # 1. Generate random data
    # For 'x': Random integers between 0 and 100
    x_data = np.random.randint(0, 101, num_rows)
    # For 'y': Random floats between 0.0 and 1.0
    y_data = np.random.rand(num_rows)

    # 2. Create a Pandas DataFrame for easy handling
    df = pd.DataFrame({"x": x_data, "y": y_data})

    # 3. Define file names (they will be saved in the current directory)
    csv_file_name = "random_data.csv"
    txt_file_name = "random_data.txt"

    # 4. Save to CSV
    df.to_csv(
        csv_file_name, index=False
    )  # index=False prevents writing the DataFrame index as a column
    print(f"Data saved successfully to: {csv_file_name}")

    # 5. Save to TXT
    # Using df.to_csv with a tab delimiter for the TXT file
    df.to_csv(
        txt_file_name, index=False, sep="\t", header=True
    )  # Using tab as separator, include header
    print(f"Data saved successfully to: {txt_file_name}")


# --- Example Usage ---
if __name__ == "__main__":
    num_data_points = 50  # You can change this number
    generate_and_save_random_data(num_data_points)

    print("\nCheck the current directory for 'random_data.csv' and 'random_data.txt'.")
