import pandas as pd

# Load the dataset (corrected filename)
df = pd.read_csv("Employee-Attrition.csv")

# Calculate basic attrition rate
attrition_rate = len(df[df["Attrition"] == "Yes"]) / len(df)
print(f"Attrition Rate: {attrition_rate:.2%}")

# Count of attrition by department
dept_counts = df[df["Attrition"] == "Yes"]["Department"].value_counts()
print("\nAttrition Count by Department:")
print(dept_counts)
