#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree


# In[2]:



df_data_or = pd.read_csv(r'C:\Users\gaura\Desktop\OnlineRetail.csv', sep=",", encoding="ISO-8859-1", header=0)
df_data_or.head()


# In[3]:


df_data_or.shape


# In[4]:


df_data_or.info()


# In[5]:


df_data_or.describe()


# In[6]:


df_data_or.isnull().sum()


# In[7]:


fig, ax = plt.subplots(figsize=(30,10)) 
sns.heatmap(df_data_or.isnull(),yticklabels = False,cbar = False, cmap = "Blues",linecolor = "Black")


# In[8]:


df_data_or = df_data_or.dropna()
df_data_or.shape


# In[9]:


df_data_or_null = df_data_or.isnull().sum()


# In[10]:


df_data_or_null


# our data is in good condition now we will work in this data

# In[11]:


df_data_or['InvoiceDate'] = pd.to_datetime(df_data_or['InvoiceDate'],format='%d-%m-%Y %H:%M')


# In[12]:


max_date = max(df_data_or['InvoiceDate'])
max_date


# In[13]:


df_data_or['Difference'] = max_date - df_data_or['InvoiceDate']
df_data_or.head(10)


# In[14]:


recfremon_r = df_data_or.groupby('CustomerID')['Difference'].min()
recfremon_r = recfremon_r.reset_index()
recfremon_r.head(10)


# In[15]:


recfremon_r['Difference'] = recfremon_r['Difference'].dt.days
recfremon_r.head(10)


# In[16]:


plt.subplots(figsize=(15, 5))
sns.histplot(recfremon_r.groupby('CustomerID')['Difference'].max(), kde=False, bins=80)
plt.title('Recency Value Distribution', fontsize = 15)
plt.xlabel('Recency')
plt.ylabel('Count');


# In[17]:


recfremon_f = df_data_or.groupby('CustomerID')['InvoiceNo'].count()
recfremon_f = recfremon_f.reset_index()
recfremon_f.columns = ['CustomerID', 'Frequency']
recfremon_f.head(10)


# In[18]:


plt.figure(figsize=(15, 5))
sns.histplot(recfremon_f.groupby('CustomerID')['Frequency'].max(), kde=False, bins=200)
plt.title('Frequency Value Distribution', fontsize = 15)
plt.xlim(-10, 1000)
plt.xlabel('Frequency')
plt.ylabel('Count');


# In[19]:


recfremon = pd.merge(recfremon_r, recfremon_f, on='CustomerID', how='inner')
recfremon.head(10)


# In[20]:


df_data_or['Amount'] = df_data_or['UnitPrice']*df_data_or['Quantity']
recfremon_m = df_data_or.groupby('CustomerID')['Amount'].sum()
recfremon_m = recfremon_m.reset_index()
recfremon_m.head(10)


# In[21]:


plt.subplots(figsize=(15, 5))
sns.histplot(recfremon_m.groupby('CustomerID')['Amount'].max(), kde=False, bins=400)
plt.title('Monetary Value Distribution', fontsize = 15)
plt.xlim(-10000, 40000)
plt.xlabel('Amount')
plt.ylabel('Count');


# In[22]:


recfremon = pd.merge(recfremon, recfremon_m, on='CustomerID', how='inner')
recfremon.columns = ['CustomerID', 'Recency', 'Frequency', 'Amount']
recfremon.head(10)


# In[23]:


sns.boxplot(data = recfremon['Recency'])
plt.title("Outliers Variable Distribution", fontsize = 14, fontweight = 'bold')
plt.ylabel("Range", fontweight = 'bold')
plt.xlabel("Recency", fontweight = 'bold')


# In[24]:


sns.boxplot(data = recfremon['Frequency'])
plt.title("Outliers Variable Distribution", fontsize = 14, fontweight = 'bold')
plt.ylabel("Range", fontweight = 'bold')
plt.xlabel("Frequency", fontweight = 'bold')


# In[25]:


sns.boxplot(data = recfremon['Amount'])
plt.title("Outliers Variable Distribution", fontsize = 14, fontweight = 'bold')
plt.ylabel("Range", fontweight = 'bold')
plt.xlabel("Amount", fontweight = 'bold')


# In[26]:


Q1 = recfremon.Recency.quantile(0.05)
Q3 = recfremon.Recency.quantile(0.95)
IQR = Q3 - Q1
recfremon = recfremon[(recfremon.Recency >= Q1 - 1.5*IQR) & (recfremon.Recency <= Q3 + 1.5*IQR)]


# In[27]:


Q1 = recfremon.Frequency.quantile(0.05)
Q3 = recfremon.Frequency.quantile(0.95)
IQR = Q3 - Q1
recfremon = recfremon[(recfremon.Frequency >= Q1 - 1.5*IQR) & (recfremon.Frequency <= Q3 + 1.5*IQR)]


# In[28]:


Q1 = recfremon.Amount.quantile(0.05)
Q3 = recfremon.Amount.quantile(0.95)
IQR = Q3 - Q1
recfremon = recfremon[(recfremon.Amount >= Q1 - 1.5*IQR) & (recfremon.Amount <= Q3 + 1.5*IQR)]


# In[29]:


recfremon_df = recfremon[['Recency', 'Frequency', 'Amount']]

scale = StandardScaler()

recfremon_df_scaled = scale.fit_transform(recfremon_df)
recfremon_df_scaled.shape


# In[30]:


recfremon_df_scaled = pd.DataFrame(recfremon_df_scaled)
recfremon_df_scaled.columns = ['Recency', 'Frequency', 'Amount']
recfremon_df_scaled.head()


# In[31]:


km = KMeans(n_clusters=4, max_iter=50)
km.fit(recfremon_df_scaled)


# In[32]:


km.labels_


# In[33]:



ssd = []
range_n_clusters =range(1,9)
for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(recfremon_df_scaled)
    
    ssd.append(kmeans.inertia_)
    

plt.plot(range(1,9),ssd,marker='o')
plt.show()


# In[34]:


kmeans = KMeans(n_clusters=3, max_iter=50)
kmeans.fit(recfremon_df_scaled)


# In[35]:


kmeans.labels_


# In[36]:


recfremon['Cluster_Id'] = kmeans.labels_
recfremon.head()


# In[37]:


sns.boxplot(x='Cluster_Id', y='Recency', data=recfremon)


# In[38]:


sns.boxplot(x='Cluster_Id', y='Frequency', data=recfremon)


# In[39]:


sns.boxplot(x='Cluster_Id', y='Amount', data=recfremon)


# In[40]:


mergings = linkage(recfremon_df_scaled, method="complete", metric='euclidean')
dendrogram(mergings)
plt.show()


# In[41]:


cluster_labels = cut_tree(mergings, n_clusters=3).reshape(-1, )
cluster_labels


# In[42]:


recfremon['Cluster_Labels'] = cluster_labels
recfremon.head()


# In[43]:


sns.boxplot(x='Cluster_Labels', y='Recency', data=recfremon)


# In[44]:


sns.boxplot(x='Cluster_Labels', y='Frequency', data=recfremon)


# In[45]:


sns.boxplot(x='Cluster_Labels', y='Amount', data=recfremon)

