#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv("diabetes.csv")


# In[3]:


df


# In[4]:


inputs=df.drop('Outcome',axis='columns')
target=df['Outcome']


# In[5]:


BloodPressure_rating= []
for row in df['BloodPressure']:
    if row <80: BloodPressure_rating.append('Normal')
    elif 80<=row<90: BloodPressure_rating.append('High_stage1')
    elif 90<=row<120: BloodPressure_rating.append('High_stage2')
    else :BloodPressure_rating.append('Crisis')


# In[6]:


df['BloodPressure_rating']= BloodPressure_rating


# In[7]:


print(df)


# In[8]:


df['BloodPressure_rating'].value_counts()


# In[27]:


#threshhold= input("Enter threshhold")
threshold=0.12
count1=len(df[(df.BloodPressure_rating=='Normal')])
count2=len(df[(df.BloodPressure_rating=='High_stage1')])
count3=len(df[(df.BloodPressure_rating=='High_stage2')])
count4=len(df[(df.BloodPressure_rating=='Crisis')])
High_occurrence = []
for row in df['BloodPressure_rating']:
    if row=='Normal' and threshold<=(count1/767): High_occurrence.append('True')
    elif row=='Normal' and threshold>(count1/767): High_occurrence.append('False')
    if row=='High_stage1' and threshold<=(count2/767): High_occurrence.append('True')
    elif row=='High_stage1' and threshold>(count2/767): High_occurrence.append('False')
    if row=='High_stage2' and threshold<=(count3/767): High_occurrence.append('True')
    elif row=='High_stage2' and threshold>(count3/767): High_occurrence.append('False')
    if row=='Crisis' and threshold<=(count4/767): High_occurrence.append('True')
    elif row=='Crisis' and threshold>(count4/767): High_occurrence.append('False')


# In[28]:


df['High_occurrence']=High_occurrence


# In[31]:


pd.set_option('display.max_rows', None)
df


# In[ ]:




