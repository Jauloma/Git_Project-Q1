#!/usr/bin/env python
# coding: utf-8

# ## <center> Individual Project
# ### Week 8
# ### <i> By Jacob Oriang Jaroya

# #### In the peer programming project, we created a data frame representing our store’s products and sales. In
# #### this exercise, we’re going to extend that data frame, quite literally.
# 
# 
# #### The backstory for this exercise is as follows: Our local government is thinking about imposing a
# #### sales tax, and is thinking about 15, 20, and 25 percent rates. Show how much less you would net
# ####  with each of these tax amounts by adding columns to the data frame for current income, as well.

# In[1]:


import pandas as pd


# In[2]:


sales_dict=[{'product_id':23, 'name':'computer', 'wholesale_price': 500, 'retail_price':1000, 'sales':100}, 
{'product_id':96, 'name':'Python Workout', 'wholesale_price': 35,'retail_price':75, 'sales':1000},
{'product_id':97, 'name':'Pandas Workout', 'wholesale_price': 35, 'retail_price':75, 'sales':500},
{'product_id':15, 'name':'banana', 'wholesale_price': 0.5,'retail_price':1, 'sales':200},
{'product_id':87, 'name':'sandwich', 'wholesale_price': 3,'retail_price':5, 'sales':300}]


# In[3]:


# creating dataframe from "my_dict"
sales_df = pd.DataFrame(sales_dict)


# In[4]:


# Displaying "my_df" DataFrame
print(sales_df)


# In[5]:


# How much total net revenue you received from all of these sales?
sales_df['total_net_revenue']= ((sales_df['retail_price'] - sales_df['wholesale_price']) * sales_df['sales'])
sales_df['total_net_revenue_at_15_tax'] = ((sales_df['retail_price']*0.85 - sales_df['wholesale_price']) * sales_df['sales'])
sales_df['total_net_revenue_at_20_tax'] = ((sales_df['retail_price']*0.8 - sales_df['wholesale_price']) * sales_df['sales'])
sales_df['total_net_revenue_at_25_tax']= ((sales_df['retail_price']*0.75 - sales_df['wholesale_price']) *sales_df['sales'])


# In[6]:


sales_df


# ### Working out Total Revenue before and after tax

# In[9]:


# Calculating total revenue
total_net_revenue = sales_df['total_net_revenue'].sum()
total_net_revenue_at_15_tax= sales_df['total_net_revenue_at_15_tax'].sum()
total_net_revenue_at_20_tax=sales_df['total_net_revenue_at_20_tax'].sum()
total_net_revenue_at_25_tax= sales_df['total_net_revenue_at_25_tax'].sum()


# In[10]:


print(f'Total Revenue before Tax: \t${total_net_revenue:,.2f}')
print(f'Total Revenue 15% Sales Tax: \t${total_net_revenue_at_15_tax:,.2f}')
print(f'Total Revenue 20% Sales Tax: \t${total_net_revenue_at_20_tax:,.2f}')
print(f'Total Revenue 25% Sales Tax: \t${total_net_revenue_at_25_tax:,.2f}')


# In[ ]:




