#puzzle 1
import pandas as pd
import numpy as np  # For random values

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df = df.rename(columns={"First Name": "first_name", "Age": "age"})

print("First 3 rows:")
print(df.head(3))

mean_age = df['age'].mean()
print(f"\nMean age: {mean_age}")

name_city_df = df[['first_name', 'City']]
print("\nName and City columns:")
print(name_city_df)

df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nDataFrame with salary column:")
print(df)

print("\nSummary statistics:")
print(df.describe())

#puzzle 2
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

print("Sales and Expenses DataFrame:")
print(sales_and_expenses)

max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print(f"\nMaximum Sales: {max_sales}")
print(f"Maximum Expenses: {max_expenses}")

min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print(f"\nMinimum Sales: {min_sales}")
print(f"Minimum Expenses: {min_expenses}")

avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print(f"\nAverage Sales: {avg_sales}")
print(f"Average Expenses: {avg_expenses}")
#puzzle 3
import pandas as pd

# 1. Create the expenses DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

print("Expenses DataFrame:")
print(expenses)

expenses = expenses.set_index('Category')
print("\nExpenses DataFrame with Category as index:")
print(expenses)

max_expenses = expenses.max(axis=1)
print("\nMaximum expense for each category:")
print(max_expenses)

min_expenses = expenses.min(axis=1)
print("\nMinimum expense for each category:")
print(min_expenses)

avg_expenses = expenses.mean(axis=1)
print("\nAverage expense for each category:")
print(avg_expenses)
