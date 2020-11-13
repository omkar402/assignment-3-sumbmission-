#!/usr/bin/env python
# coding: utf-8

# # Q1.Create a numpy array starting from 2 till 50 with a stepsize of 3.

# In[1]:


import numpy as np


# In[2]:



arr = np.arange(2,50,3)
print(arr)


# # Q2.Accept two lists of 5 elements each from the user.
# Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it.

# In[1]:


import numpy as np
a=[]

b=[]
total=int(input("\ntotal number wants to add in list"))
for i in range(total):
    x=int(input("\nenter number which you want add in list a"))
    y=int(input("enter number which you want add in list b"))
    a.append(x)
    b.append(y)
print(a)
print(b)
arr1=np.array(a)
arr2=np.array(b)
arr=np.concatenate((arr1,arr2))
print(arr)
print(np.sort(arr))


# # Q3.Write a code snippet to find the dimensions of a ndarray and its size.

# In[17]:


arr=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(np.ndim(arr))
print(np.size(arr))


# # Q4.How to convert a 1D array into a 2D array?

#  1.using expand_dims

# In[62]:


arr1=np.array([1,2,3,4,5,6,7,8,9,10])
arr2=np.expand_dims(arr1, axis=1)
print(arr2)
arr2.ndim




# 2.using np.newaxis,

# In[78]:


a = np.array([1, 2, 3, 4, 5, 6])
a2 = a[:,np.newaxis]
print(a2)
print(a.ndim)
print(a2.ndim)



# In[80]:


a = np.array([1, 2, 3, 4, 5, 6])
a2 = a[np.newaxis,:]
print(a2)
print(a.ndim)
print(a2.ndim)


# # Q5.Consider two square numpy arrays. Stack them vertically and horizontally.

# In[98]:


x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,89,9],[12,13,14]])
print('Horizontal Append:', '\n',np.hstack((x,y)))


# In[99]:


x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,89,9],[12,13,14]])
print('vertical Append:', '\n',np.vstack((x,y)))


# # Q6.How to get unique items and counts of unique items?

# In[111]:


arr = np.array( [10,80,20,90,30,70,40,50,60,10,70,80,90,20,100,40,100] )
print("original array",arr)
arr1=np.unique(arr,return_counts=True)
print("count of unique value",'\n',np.asarray(arr1))


# In[ ]:




