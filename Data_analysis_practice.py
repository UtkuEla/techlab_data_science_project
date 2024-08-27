#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df=pd.read_csv(r"C:\Users\flora\Desktop\gym_membership_prediction_with_professional_status.csv")


# In[7]:


df.head()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df["Gender"].value_counts()


# In[11]:


df["Membership Type"].value_counts()


# In[ ]:





# In[12]:


df["Annual Income"].mean()


# In[13]:


df["Health Condition"].value_counts()


# In[14]:


mem_grp=df.groupby(["Membership Type"])
mem_grp.get_group("Premium")


# In[15]:


print("\nDescriptive statistics of Price:\n")
stats=df["Annual Income"].describe()
print(stats)


# In[16]:


mem_grp["Annual Income"].value_counts().loc["Premium"].head(50)


# 

# In[17]:


women_members=mem_grp["Gender"].apply(lambda x: x.str.contains("Female").sum())
women_members


# In[18]:


guy_members=mem_grp["Gender"].apply(lambda x: x.str.contains("Male").sum())
guy_members


# In[19]:


other_members=mem_grp["Gender"].apply(lambda x: x.str.contains("Other").sum())
other_members


# In[ ]:




