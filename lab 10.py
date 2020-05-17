#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
class Animal:
    def legs(self):
        print("animals have 4 legs")
class Tiger(Animal):
    pass
class Dog(Animal):
    Animal().legs()
Tiger().legs()


# In[2]:


#Q.2
class Employee:
    def printDesignation():
        pass
class Engineer(Employee):
    def printDesignation():
        print("Engineer")
class Manager(Employee):
    def printDesignation():
        print("Manager")
Engineer.printDesignation()
Manager.printDesignation()


# In[9]:


#Q3
class Dog:

     attr1 = "mamal"
     attr2 = "dog"

     def fun(self):
         print("I'm a", self.attr1)
         print("I'm a", self.attr2)

 Rodger = Dog()

 print(Rodger.attr1, Rodger.attr2)
 print(Rodger.fun())


# In[7]:


#Q4:-

class Parent1():

    def show(self):
        print("Parent 1 statement ")

class Parent2():

    def display(self):
        print("Parent 2 statment ")

class Child(Parent1, Parent2):

    def show(self):
        print(" child statment ")


obj = Child()

obj.show()
obj.display()


# In[5]:


#Q.5
class A:
    def m(self):
        print("A")
class B:
    def n(self):
        print("B")
class C(A,B):
    def o(self):
        print("C")
x=C()
x.m()
x.n()
x.o()


# In[ ]:




