#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas
import matplotlib
import seaborn
import sklearn


# In[2]:


print(sys.version)


# In[3]:


print(pandas.__version__)


# In[5]:


print(matplotlib.__version__)


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split


# In[7]:


games= pandas.read_csv("games.csv")
#imports dataset


# In[8]:


#print names of columns
print(games.columns)
print(games.shape)


# In[9]:


#hoistogram of avg reading
plt.hist(games["average_rating"])
plt.show()


# In[10]:


#print first row of games with 0 scores
print(games[games["average_rating"]==0].iloc[0])

#scores greater than 0
print(games[games["average_rating"]>0].iloc[0])


# In[11]:


#remove any rows without user reviews
games=games[games["users_rated"]>0]

#remove rows with missing values
games=games.dropna(axis=0)

#make histogram again
plt.hist(games["average_rating"])
plt.show()


# In[12]:


print(games.columns)


# In[15]:


#id doesnt give any information and causes overfitting
#correlation matrix using seaborn

corrmat=games.corr()
fig=plt.figure(figsize=(12,9))

sns.heatmap(corrmat,vmax=0.8,square=True)
plt.show()
#shows correlations between the parameters


# In[16]:


#get all columns from dataframe
columns=games.columns.tolist()

#filtering columns
columns = [c for c in columns if c not in["bayes_average_rating","average_rating","type","name","id"]]

#store the variable predicting on
target="average_rating"


# In[18]:


#split dataset into train and test

from sklearn.model_selection import train_test_split
train=games.sample(frac=0.8, random_state=1)

#select anything not in training and put in test
test=games.loc[~games.index.isin(train.index)]

#printing shapes
print(train.shape)
print(test.shape)


# In[19]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
lrmodel=LinearRegression()
#create object of model

lrmodel.fit(train[columns],train[target])
#fits model to training data



# In[20]:


#predictions
predictions=lrmodel.predict(test[columns])

#compute mean squared error
mean_squared_error(predictions,test[target])


# In[22]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
lrmodel=LinearRegression()
#create object of model

lrmodel.fit(train[columns],train[target])
#fits model to training data

#predictions
predictions=lrmodel.predict(test[columns])

#compute mean squared error
mean_squared_error(predictions,test[target])


# In[23]:


from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_squared_error
rfmodel=RandomForestRegressor(n_estimators=100,min_samples_leaf=10,random_state=1)

#create object of model

rfmodel.fit(train[columns],train[target])
#fits model to training data

#predictions
predictions=rfmodel.predict(test[columns])

#compute mean squared error
mean_squared_error(predictions,test[target])


# In[24]:


test[columns].iloc[0]


# In[25]:


#find rating
ratinglr = lrmodel.predict(test[columns].iloc[0].values.reshape(1,-1))
ratingrf = rfmodel.predict(test[columns].iloc[0].values.reshape(1,-1))

#printing
print(ratinglr)
print(ratingrf)


# In[26]:


test[target].iloc[0]


# In[ ]:




