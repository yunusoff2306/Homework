import pandas as pd
import matplotlib.pyplot as plt

# DataFrame creation
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print("Average Grades:\n", df1[['Student_ID', 'Average']])

# Exercise 2: Find the student with the highest average grade
highest_avg = df1.loc[df1['Average'].idxmax()]
print("\nStudent with the Highest Average Grade:\n", highest_avg)

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print("\nTotal Marks for Each Student:\n", df1[['Student_ID', 'Total']])

# Exercise 4: Plot a bar chart to visualize the average grades in each subject
subject_avg = df1[['Math', 'English', 'Science']].mean()
subject_avg.plot(kind='bar', title='Average Grades in Each Subject')
plt.ylabel('Average Grade')
plt.show()

#puzzle 2
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame creation
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total Sales for Each Product:\n", total_sales)

# Exercise 2: Find the date with the highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("\nDate with the Highest Total Sales:", highest_sales_date)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day
df2[['Product_A_Pct_Change', 'Product_B_Pct_Change', 'Product_C_Pct_Change']] = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("\nPercentage Change in Sales for Each Product:\n", df2[['Date', 'Product_A_Pct_Change', 'Product_B_Pct_Change', 'Product_C_Pct_Change']])

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time
df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].plot(title='Sales Trends for Each Product')
plt.ylabel('Sales')
plt.show()
#puzzle 3
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame creation
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", avg_salary_by_dept)

# Exercise 2: Find the employee with the most experience
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with the Most Experience:\n", most_experienced_employee)

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("\nSalary Increase Percentage for Each Employee:\n", df3[['Name', 'Salary Increase (%)']])

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments
employee_count_by_dept = df3['Department'].value_counts()
employee_count_by_dept.plot(kind='bar', title='Employee Distribution by Department')
plt.ylabel('Number of Employees')
plt.show()
#puzzle
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame creation
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print("Total Revenue from All Orders:", total_revenue)

# Exercise 2: Find the most ordered product
most_ordered_product = df4['Product'].value_counts().idxmax()
print("\nMost Ordered Product:", most_ordered_product)

# Exercise 3: Calculate the average quantity of products ordered
average_quantity = df4['Quantity'].mean()
print("\nAverage Quantity of Products Ordered:", average_quantity)

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
sales_by_product.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Product')
plt.ylabel('')
plt.show()
