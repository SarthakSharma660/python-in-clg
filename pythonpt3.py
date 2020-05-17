#!/usr/bin/env python
# coding: utf-8

# In[39]:


# 1. class A(object):
#      def __init__(self):
#         print("world")
# 
#      class B(A):
#        def __init__(self):
#         print("hello")
#         super(B, self).__init__()
# 
#     B()
# BY USING SUPER


# In[22]:


#3
people = {1: {'name': 'name', 'age': '19', 'sex': 'Male'},
          2: {'name': 'fname', 'age': '24', 'sex': 'Female'}}

print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])


# In[40]:


#2
#class BaseClass:
#              Body of base class
#class DerivedClass(BaseClass):
#             Body of derived class


# In[41]:


#doing Set B Both Questions


# In[38]:


#set B Q1
phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))


# In[32]:


#Q2
lists = [12,24,35,24,88,120,155]
lists= [x for x in lists if x!=24]
print (lists)


# In[ ]:




