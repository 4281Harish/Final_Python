# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fDPDvw7kWmMAsq5I3ljPWtA_bvZvfWnr
"""

#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
df=pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
df
df.info()
df.head()
df.info()
df.describe()
df.dtypes
df.isnull().sum()
df.shape
df.size











#Q4











[102 rows x 10 columns]


#Q7 - Trend Analysis
# i)
df['Order Month'] = pd.to_datetime(df['Order Date']).dt.month
salesData = df.groupby('Order Year')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Year')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()

salesData = df.groupby('Order Month')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Month')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()




Name: TimeBetweenOrderAndDelivery, dtype: timedelta64[ns]
8 days 20:48:44.384743576
i) As of now the average time taken for the shipment of an order is 8 days and 20 hours.It stands highest for Tables delivery . Allocation of bigger trucks through optimised organisation of transporters can be introduced to improve the supply chain.
ii) The geographic distribution of sales is influenced by factors such as demographics (age, income), cultural preferences, economic conditions and local requirements. Insights from these factors can inform targeted marketing by enabling businesses to tailor products, pricing, promotions, and advertising strategies to specific regions, demographics, and consumer behaviors thus improving sales performance and customer engagement.

customer_order_amounts = df.groupby('EmailID')['Sales'].sum().reset_index()

top_10_percent = int(len(customer_order_amounts) * 0.1)
high_value_customers = customer_order_amounts.nlargest(top_10_percent, 'Sales')
print(high_value_customers)

customer_order_amounts = df.groupby('EmailID')['Quantity'].sum().reset_index()

top_10_percent = int(len(customer_order_amounts) * 0.1)
high_value_customers = customer_order_amounts.nlargest(top_10_percent, 'Quantity')
print(high_value_customers)

for index, customer in high_value_customers.iterrows():
  pass
  #We can write a function to send promotional offers to these value customers





[68 rows x 2 columns]
iii) High value customers can be identified by their purchasing quantity, purchase frequency and pruchase amount . These customers can be given additional promotions and offers to enhance customer loyalty and they are more likely to recommend wallmart to other potential customers

#2

print("Number of Missing Values in given data set:")


print(df.isnull().sum())
#no missing values
df.drop_duplicates(inplace=True)


# we don't have any missing values thats why we are not doing any operations here

#3

print("Mean: Sales \n", df['Sales'].mean())
print("Median: Sales \n", df['Sales'].median())
print("Mode: Sales \n", df['Sales'].mode())
print("Range: Sales \n", df['Sales'].max() - df['Sales'].min())
print("Variance: Sales \n", df['Sales'].var())
print("Standard Deviation: Sales \n", df['Sales'].std())
print("Mean: Quantity \n", df['Quantity'].mean())
print("Median: Quantity \n", df['Quantity'].median())
print("Mode: Quantity \n", df['Quantity'].mode())
print("Range: Quantity \n", df['Quantity'].max() - df['Quantity'].min())
print("Variance: Quantity \n", df['Quantity'].var())
print("Standard Deviation: Quantity \n", df['Quantity'].std())
print("Mean: Profit \n", df['Profit'].mean())
print("Median: Profit \n", df['Profit'].median())
print("Mode: Profit \n", df['Profit'].mode())
print("Range: Profit \n", df['Profit'].max() - df['Profit'].min())
print("Variance: Profit \n", df['Profit'].var())
print("Standard Profit: Profit \n", df['Profit'].std())

#4
# result=df.groupby(df['Category']).agg({"Category":'count'})

# plt.pie(result['Category'],labels=result['Category'])
# plt.legend()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Order Year'] = pd.to_datetime(df['Order Date']).dt.year


salesData = df.groupby('Order Year')['Sales'].sum()
salesData.plot(label='Sales')
profitData = df.groupby('Order Year')['Profit'].sum()
profitData.plot(label='Profit')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='Profit', data=df)
plt.title('Profit vs Quantity')
plt.xlabel('Quantity')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Profit', data=df)
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.tight_layout()
plt.show()

#5
print("Correlation Between Different Columns is :")
print(df.corr())

df.shape
#Correlation plot
sns.heatmap(df.corr())

#6
import pandas as pd
import matplotlib.pyplot as plt




numeric_cols = ['Sales', 'Quantity', 'Profit']
df_zscores = df[numeric_cols].apply(lambda x: np.abs((x - x.mean()) / x.std()))

outliers = df_zscores > 3

outliers_data = df[outliers.any(axis=1)]

print("Outliers:")
print(outliers_data)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numeric_cols])
plt.title('Boxplot of Sales, Quantity, and Profit')
plt.xlabel('Features')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Trend Analysis
#7i
df=pd.read_excel("/content/Walmart_Dataset Python_Final_Assessment.xlsx")
df['Order Date'] = pd.to_datetime(df['Ship Date'])
df.set_index('Ship Date', inplace=True)
yearly_data = df.resample('Y').sum()
plt.figure(figsize=(10, 6))
plt.plot(yearly_data.index.year, yearly_data['Sales'], label='Sales')
plt.plot(yearly_data.index.year, yearly_data['Profit'], label='Profit')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Sales and Profit Trends Over Years')
plt.legend()
plt.grid(True)
plt.show()

#7ii

import pandas as pd


df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Date'] = df['Order Date'].dt.year

yearly_category_sales = df.groupby(['Order Date', 'Category'])['Sales'].sum().reset_index()
pivot_table = yearly_category_sales.pivot(index='Order Date', columns='Category', values='Sales')

growth_rate = pivot_table.pct_change(axis='rows') * 100

growth_overall = growth_rate.sum()
most_growing_category = growth_overall.idxmax()

print("Product category with the most growth in terms of sales over the years:", most_growing_category)

#Customer Analysis
#7i
customer_summary = df.groupby('EmailID').agg({'Order ID': 'nunique', 'Sales': 'sum'}).reset_index()
customer_summary.columns = ['EmailID', 'Quantity', 'TotalSales']

top_customers_by_orders = customer_summary.nlargest(5, 'Quantity')
top_customers_by_sales = customer_summary.nlargest(5, 'TotalSales')

print("Top 5 Customers by Orders Placed:")
print(top_customers_by_orders.set_index('EmailID'))
print("\nTop 5 Customers by Total Sales:")
print(top_customers_by_sales.set_index('EmailID'))
#EmailID
#Insights - Customers who tend to spend more , spend them on less number of products and customers who tend to buy more tend to spend less on each product.

#7ii
df['OrderDate'] = pd.to_datetime(df['Order Date'])
df.sort_values(by=['EmailID', 'Order Date'], inplace=True)
df['TimeBetweenOrders'] = df.groupby('EmailID')['Order Date'].diff()
average_time_between_orders = df.groupby('EmailID')['TimeBetweenOrders'].mean()

print("Average Time Between Orders for Each Customer:")
print(average_time_between_orders)
print(average_time_between_orders.mean())

"""#Comprehensive Analysis"""
#7i

#average Time between order and delivery
df['TimeBetweenOrderAndDelivery'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('Category')['TimeBetweenOrderAndDelivery'].mean()
print(average_time_between_order_and_delivery)

df['TimeBetweenOrderAndDelivery'] = df['Ship Date'] - df['Order Date']
average_time_between_order_and_delivery = df.groupby('EmailID')['TimeBetweenOrderAndDelivery'].mean()
print(average_time_between_order_and_delivery.mean())

#### i)

import plotly.express as px
fig = px.scatter_geo(df, locations="Geography", locationmode="USA-states",
                      hover_name="Product Name", size="Sales", color="Sales",
                      scope="usa", title="Geographical Distribution")
fig.show()
#Places cannot be plotted because of lack of lat long.

#### ii)

customer_order_amounts = df.groupby('EmailID')['Sales'].sum().reset_index()

top_10_percent = int(len(customer_order_amounts) * 0.1)
high_value_customers = customer_order_amounts.nlargest(top_10_percent, 'Sales')
print("High value Customers based on purchase Value:")
print(high_value_customers)

customer_order_amounts = df.groupby('EmailID')['Quantity'].sum().reset_index()

top_10_percent = int(len(customer_order_amounts) * 0.1)
high_value_customers = customer_order_amounts.nlargest(top_10_percent, 'Quantity')
print("High value Customers based on purchase Quantity:")
print(high_value_customers)

df.sort_values(by=['EmailID', 'Order Date'], inplace=True)
df['TimeBetweenOrders'] = df.groupby('EmailID')['Order Date'].diff()
average_time_between_orders = df.groupby('EmailID')['TimeBetweenOrders'].mean()
print("High value Customers based on purchase Frequency:")
print(average_time_between_orders.nsmallest(top_10_percent))

for index, customer in high_value_customers.iterrows():
  pass
  #We can write a function to send promotional offers to these value customers




"""### iii) High value customers can be identified by their purchasing quantity, purchase frequency and pruchase amount .
 These customers can be given additional promotions and offers to enhance customer loyalty and they are more likely to recommend wallmart to other potential customers"""