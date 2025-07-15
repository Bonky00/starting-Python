import pandas as pd
import matplotlib.pyplot as plt  # This imports the plotting module

# Create the same sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data)

# --- Let's create a simple bar chart of Ages ---
plt.figure(figsize=(8, 5))  # Create a figure (the overall window for the plot)
plt.bar(
    df["Name"], df["Age"], color="skyblue"
)  # Create a bar chart: Names on X, Ages on Y

plt.xlabel("Person")  # Label for the horizontal axis
plt.ylabel("Age")  # Label for the vertical axis
plt.title("Ages of Our Friends")  # Title of the plot
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Add a light grid for readability

plt.show()  # Display the plot! This command is essential to make the plot appear

# --- Let's create a scatter plot of Age vs. a hypothetical 'Score' ---
# (Let's add a 'Score' column to our DataFrame for this example)
df["Score"] = [85, 92, 78, 95]

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Age"], df["Score"], color="red", s=100, alpha=0.8, edgecolors="black"
)  # s is size of points
plt.xlabel("Age")
plt.ylabel("Score")
plt.title("Age vs. Score for Our Friends")
plt.grid(True)  # Add a grid
plt.savefig("example image.png")  # Display this plot too!
