#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected = True)

from matplotlib import colors 
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('whitegrid')


# In[57]:


df = pd.read_csv("timesData.csv")


# In[58]:


df.head(10)


#  Information about data

# In[59]:


df.info()


# Check the null values

# In[60]:


df.isnull().sum()


# In[61]:


df.describe().T


# In[62]:


plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), annot=True)


# In[63]:


df1 = df.iloc[:50,:]

tr1 = go.Scatter(x = df1.world_rank,
                 y = df1.citations,
                 mode = 'lines+markers',
                 name = 'income',
                 marker = dict(color = 'Red'),
                 text = df1.university_name)

tr2 = go.Scatter(x = df1.world_rank,
                 y = df1.teaching,
                 mode = 'lines+markers',
                 name = 'Teaching',
                 marker = dict(color = 'SteelBlue'),
                 text = df1.university_name)

data = [tr1,tr2]
layout = dict(title = 'Top 50 university - Income and Teaching',
              title_x = 0.5,
              template = "plotly_white",
              title_font = dict(size = 16, color = 'DarkBlue'),
              xaxis = dict(title = 'World Rank'))

fig = go.Figure(data = data, layout = layout)
fig.show()


# In[64]:


df['year'].unique()


# In[65]:


df2014 = df[df.year==2014].iloc[:20,:]
df2015 = df[df.year==2015].iloc[:20,:]
df2016 = df[df.year==2016].iloc[:20,:]



tr1 = go.Scatter(x = df2014.world_rank,
                 y = df2014.research,
                 mode = 'markers',
                 name = '2014',
                 marker = dict(color = 'Pink',size = 12),
                 text = df2014.university_name)

tr2 = go.Scatter(x = df2015.world_rank,
                 y = df2015.research,
                 mode = 'markers',
                 name = '2015',
                 marker = dict(color = 'SteelBlue',size = 12),
                 text = df2015.university_name)

tr3 = go.Scatter(x = df2016.world_rank,
                 y = df2016.research,
                 mode = 'markers',
                 name = '2016',
                 marker = dict(color = 'Red',size = 12),
                 text = df2016.university_name)

data = [tr1,tr2,tr3]
layout = dict(title = 'Top 20 universities - Research vs World rank in 2014, 2015 and 2016',
              title_x = 0.5,
              title_font = dict(size= 16, color = 'DarkBlue'),
              template = 'plotly_white',
              xaxis = dict(title = 'World Rank'),
              yaxis = dict(title = 'Research'))

fig = go.Figure(data = data, layout = layout)

fig.show()


# In[66]:


dfcountry = df['country'].value_counts().reset_index().head(20)
fig = px.bar(dfcountry, 
             x = 'index', 
             y = 'country', 
             color = 'country',
             color_continuous_scale = 'agsunset',
             labels = {'index':'Country','country':'Count'})

fig.update_layout(title = 'Top 20 Countries with the most university',
                  title_x = 0.5,
                  title_font = dict(size = 16, color = 'black'))
fig.show()


# In[67]:


df2016 = df.country[df.year == 2016]

color_list=  ['DarkBlue','LightBlue','MediumAquamarine','Plum','OrangeRed','DarkRed','Pink','LightGoldenrodYellow']

colormap = colors.ListedColormap(color_list)

plt.rcParams['figure.figsize'] = (15, 15)

wordcloud =  WordCloud(background_color= 'black',width = 1200,height = 800 ,max_words = 120,colormap = colormap ).generate(" ".join(df2016))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# In[68]:


plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), annot=True)


# In[ ]:





# In[ ]:




