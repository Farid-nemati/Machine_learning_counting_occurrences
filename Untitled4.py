#!/usr/bin/env python
# coding: utf-8

# In[1]:


import padas as pd


# In[2]:


import pandas as pd


# In[3]:


df= pd.read_csv("diabetes.csv")


# In[4]:


df


# In[5]:


inputs=df.drop('Outcome',axis='columns')
target=df['Outcome']


# In[6]:


BloodPressure_rating= []
for row in df['BloodPressure']:
    if row <80: BloodPressure_rating.append('Normal')
    elif 80<=row<90: BloodPressure_rating.append('High_stage1')
    elif 90<=row<120: BloodPressure_rating.append('High_stage2')
    else :BloodPressure_rating.append('Crisis')


# In[7]:


df['BloodPressure_rating']= BloodPressure_rating


# In[8]:


print(df)


# In[9]:


df['BloodPressure_rating'].value_counts()


# In[13]:


#threshold is 0.18
High_occurrence = []
for row in df['BloodPressure_rating']:
    if row=='Normal': High_occurrence.append('True')
    elif row=='High_stage1': High_occurrence.append('True')
    else :High_occurrence.append('False')


# In[14]:


df['High_occurrence']=High_occurrence


# In[15]:


df


# In[ ]:




