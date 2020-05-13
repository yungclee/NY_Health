#!/usr/bin/env python
# coding: utf-8



## source code from NY department of Health
#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("health.data.ny.gov", 
                "QQWlaoGFZYkDunsiGCH6mFvsO",
                username = "jasean12@gmail.com",
                password = "Asd0911221124")

# dictionaries by sodapy.
results = client.get("u4ud-w55t", limit = 4000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)


# In[63]:


import seaborn as sns
from eda import EDA
import matplotlib.pyplot as plt
results_df.columns


# In[65]:


#convert charges and costs into numeric
numeric_cols = ['total_charges','total_costs', 'length_of_stay']
results_df[numeric_cols ] = results_df[numeric_cols ].apply(pd.to_numeric, errors='coerce')
categorical_cols = ['gender','race','ethnicity','type_of_admission']
results_df[categorical_cols] = results_df[categorical_cols].astype('category')


# In[66]:


results_df.info()


# In[67]:


results_df.describe()


# In[68]:


sns.distplot(results_df['total_charges'])


# In[47]:


sns.distplot(results_df['total_costs'])


# In[48]:


sns.distplot(results_df['total_costs'] / results_df['total_charges'])


# In[69]:


results_df[['age_group','gender','race','length_of_stay','total_charges','total_costs']].corr()


# In[70]:


EDA(results_df)

