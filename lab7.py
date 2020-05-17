#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multi(x,y)
    print(x*y)


# In[2]:


#Q1 
def add_num(a,b):
    multiply=a*b;
    return multiply;
num1=int(input("input the number one: "))
num2=int(input("input the number one: "))
print("The product is",add_num(num1,num2))


# In[4]:


#Q2 
def sum_num(a,b):
    add=a+b;
    return add;
num1=int(input("input the number one: "))
num2=int(input("input the number one: "))
print("The sum is",sum_num(num1,num2))


# In[5]:


#Q3
def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    return fact   
number=int(input("Please enter any number to find factorial: "))
result=factorial(number)
print("The factorial of %d = %d"%(number,result))


# In[6]:


#Q4
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[8]:


#Q5
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    
    print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))
 
num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
swap_numbers(num1, num2)


# In[10]:


#Q6
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input(" Please Enter the First Number : ")) 
num2 = int(input(" Please Enter the Second Number : "))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[11]:


c = (input(" Please Enter the Alphabet : ")) 
print("The ASCII value of '" + c + "' is", ord(c))


# In[13]:


abs(-7)
any((1,0,0))


# In[14]:


#Q9
import datetime 
from datetime import date  
print ("Present date is : ",end="") 
print (date.today())


# In[15]:


#Q11
def student(firstname, lastname):  
     print(firstname, lastname)  
    
                    
student(firstname ='Sarthak', lastname ='Sharma')     
student(lastname ='Sharma', firstname ='Sarthak')


# In[16]:


#Q12
 # Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 
myFun(10)


# In[17]:


#Q13
# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Sarthak', 'is', 'good', 'Boy :)')


# In[19]:



#Q10
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# In[ ]:




