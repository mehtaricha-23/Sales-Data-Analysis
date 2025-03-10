import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv')
print(df.head())

# Checking for missing value
missing_value = df.isnull().sum()
print(missing_value)

# Removing the duplicates rows
df.drop_duplicates()

# Converting the orderdate to datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
print(df['OrderDate'])

#For finding thr data summery
print(df.describe())
print(df.info())

# Find the total order
total_order = df['OrderID'].nunique()
print('total order :',total_order)

# Add the column revenue
df['revenue'] = df['Quantity'] * df['Price']

# Total revenue generate
total_revenue = df['revenue'].sum()
print('Total revenue',total_revenue)

#Product-wise aggregation
product_summary= df.groupby('ProductName').agg({"Quantity": "sum" , "revenue" :"sum"})
print(product_summary)

# Find the top maximum revenue products
top_products = product_summary.sort_values(by='revenue',ascending=False)
print(top_products)

plt.figure(figsize=(10,6))
sns.barplot(x = top_products.index,y = top_products['revenue'],palette = 'viridis')
plt.xlabel("Product Name")
plt.ylabel("Total Revenue")
plt.title("Top 5 Best-Selling Products By Revenue")
plt.xticks(rotation = 45)
plt.show()

df['Month'] = df['OrderDate'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['revenue'].sum()
print(monthly_revenue) 

plt.figure(figsize=(10, 6))
monthly_revenue.index = monthly_revenue.index.to_timestamp()  # Convert period to timestamp for better plotting
plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.title("Monthly Revenue Trend")
plt.grid(True)
plt.show()