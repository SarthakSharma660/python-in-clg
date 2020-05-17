#!/usr/bin/env python
# coding: utf-8

# In[6]:


# ### VIVA QUESTIONS
# 

# Q1.
# 
# i- For I in range (0,4): print I
# 
# Ans. In this , it will print the first 4 numbers in the list.
# 
# ii- For I in list: print I
# 
# Ans. In this , it will print all the numbers of the list.
# 
# Q2. 
# Ans. 'abcdefghij' will be printed.
# 
# Q3.
# Ans. A list can be converted into string by using Join Operator. 


# In[7]:


#### PROGRAMMING QUESTIONS


# In[8]:


#ques1
list1=[10,24,11,45,68,91,131]
prime=[]
evens=[]
odds=[]
positive=[]
negative=[]
zeroes=[]

for i in list1:
    isprime = True
    for num in range(2,i):
        if i % num == 0:
            isprime = False
            
    if  isprime:
        prime.append(i)
    
    if(i%2==0):
        evens.append(i)
    else:
        odds.append(i)
    if(i>0):
        positive.append(i)
    elif(i==0):
        zeroes.append(i)
    else:
        negative.append(i)
        
#ques1(a)part
print("primes are :",prime)
print("even:",evens)
print("odd:",odds)
print("positive:",positive)
print("negative:",negative)
print("zeroes:",zeroes)

##ques1(b)part
final_list=zeroes+positive+evens+negative+odds+prime
final_list

##ques1(c)part
def bubblesort(arr):
    n =len(arr)
    
    for i in range(n):
        
        for j in range(0,n-i-1):
            if arr[j]>arr[j-1]:
                arr[j],arr[j-1]= arr[j-1],arr[j]
bubblesort(final_list)

print(final_list)


# In[ ]:




