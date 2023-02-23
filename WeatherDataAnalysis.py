#!/usr/bin/env python
# coding: utf-8

#  # Weather Data Analysis using python 

# In[6]:


import pandas as pd


# In[12]:


data = pd.read_csv("E:\Weather Data.csv")


# In[17]:


data.head()


# In[19]:


data.index


# In[18]:


data.shape


# In[21]:


data.columns


# In[23]:


data.dtypes


# In[27]:


data['Weather'].unique()


# In[32]:


data.count()


# In[28]:


data.nunique()


# In[33]:


data['Weather'].value_counts()


# In[34]:


data.info()


# # Q.1)  Find all the unique 'Wind Speed' values in the data.

# In[35]:


data['Wind Speed_km/h'].unique()


# # Q. 2) Find the number of times when the 'Weather is exactly Clear'.

# In[48]:


data[data['Weather'] == 'Clear'].count()


# # Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[53]:


data[data['Wind Speed_km/h'] ==4 ]


# # Q. 4) Find out all the Null Values in the data.

# In[55]:


data.isnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[56]:


data.rename(columns={'Weather': 'Weather Condition'},inplace = True)


# In[57]:


data.head()


# # Q. 6) What is the mean 'Visibility' ?

# In[59]:


data['Visibility_km'].mean()


# # Q. 7) What is the Standard Deviation of 'Pressure'  in this data?

# In[61]:


data.Press_kPa.std()


# # Q. 8) What is the Variance of 'Relative Humidity' in this data ?

# In[64]:


data['Rel Hum_%'].var()


# # Q. 9) Find all instances when 'Snow' was recorded.

# In[68]:


data.groupby('Weather Condition').get_group('Snow')


# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[75]:


data[(data['Wind Speed_km/h'] > 24 ) & (data['Visibility_km'] == 25) ]


# # Q. 11) What is the Mean value of each column against each 'Weather Condition ?

# In[76]:


data.head()


# In[77]:


data.groupby('Weather Condition').mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?

# In[78]:


data.groupby('Weather Condition').min()


# In[79]:


data.groupby('Weather Condition').max()


# # Q. 13) Show all the Records where Weather Condition is Fog.

# In[80]:


data.groupby('Weather Condition').get_group('Fog')


# # Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[82]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# # Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'

# In[83]:


data.head(2)


# In[84]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km']> 40)]

