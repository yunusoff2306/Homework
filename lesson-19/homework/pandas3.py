import pandas as pd
import sqlite3

# Load Sales Data
sales_data_path = '/mnt/data/sales_data.csv'
sales_df = pd.read_csv(sales_data_path)

# 1. Sales Data Analysis
sales_summary = sales_df.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity_Sold=('Quantity', 'max')
).reset_index()

# 2. Top Selling Product in Each Category
top_products = sales_df.groupby(['Category', 'Product']).agg(
    Total_Sold=('Quantity', 'sum')
).reset_index()
top_products = top_products.loc[top_products.groupby('Category')['Total_Sold'].idxmax()]

# 3. Date with Highest Total Sales
sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']
top_sales_date = sales_df.groupby('Date')['Total_Sales'].sum().idxmax()

# Load Customer Orders Data
customer_orders_path = '/mnt/data/customer_orders.csv'
customer_df = pd.read_csv(customer_orders_path)

# 1. Customers with at least 20 orders
customer_counts = customer_df.groupby('CustomerID').size().reset_index(name='Order_Count')
active_customers = customer_counts[customer_counts['Order_Count'] >= 20]

# 2. Customers who ordered products with an average price > 120
customer_avg_price = customer_df.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = customer_avg_price[customer_avg_price['Price'] > 120]

# 3. Products with at least 5 units sold
total_product_sales = customer_df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('Price', 'sum')
).reset_index()
popular_products = total_product_sales[total_product_sales['Total_Quantity'] >= 5]

# Load Population Data from SQLite
db_path = '/mnt/data/population.db'
conn = sqlite3.connect(db_path)
query = "SELECT * FROM population"
population_df = pd.read_sql(query, conn)
conn.close()

# Load Salary Bands
salary_band_path = '/mnt/data/population_salary_analysis.xlsx'
salary_bands = pd.read_excel(salary_band_path)

# Function to categorize salaries
def categorize_salary(salary, bands):
    for _, row in bands.iterrows():
        min_salary, max_salary = map(int, row['Salary Band'].split('-'))
        if min_salary <= salary <= max_salary:
            return row['Category']
    return 'Unknown'

# Apply Salary Categorization
population_df['Salary_Category'] = population_df['Salary'].apply(lambda x: categorize_salary(x, salary_bands))

# Aggregate statistics by salary category
salary_analysis = population_df.groupby('Salary_Category').agg(
    Percentage=('Salary', lambda x: len(x) / len(population_df) * 100),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Population_Count=('Salary', 'count')
).reset_index()

# Aggregate statistics by state
state_salary_analysis = population_df.groupby(['State', 'Salary_Category']).agg(
    Percentage=('Salary', lambda x: len(x) / len(population_df) * 100),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Population_Count=('Salary', 'count')
).reset_index()

# Display Results
print("Sales Summary:")
print(sales_summary)
print("\nTop Selling Products:")
print(top_products)
print("\nDate with Highest Sales:", top_sales_date)
print("\nActive Customers:")
print(active_customers)
print("\nHigh Value Customers:")
print(high_value_customers)
print("\nPopular Products:")
print(popular_products)
print("\nSalary Analysis:")
print(salary_analysis)
print("\nState-wise Salary Analysis:")
print(state_salary_analysis)
