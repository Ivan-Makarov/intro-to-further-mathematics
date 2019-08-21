#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[35]:


x = np.linspace(-10, 10, 200)
k = float(input('Input k2:'))
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(k*x))

