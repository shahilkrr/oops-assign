#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1


# In[20]:


class vehicle :
    def __init__(self,vehicle_name,max_speed,average):
        self.vehicle_name = vehicle_name
        self.max_speed = max_speed
        self.average = average


# In[21]:


Hyundai = vehicle('Verna',170,12)


# In[22]:


Hyundai.average


# In[25]:


Hyundai.vehicle_name


# In[26]:


#Question 2


# In[27]:


class car(vehicle):
    def seating_capacity(self,seating_capacity):
        return f"The {self.vehicle_name} has seating capacity of {seating_capacity} peoples."


# In[30]:


Kia = car('Sonet',140,10)


# In[32]:


Kia.seating_capacity(5)


# In[33]:


#Question 3


# When a class is derived from more than one superclass is called multiple inheritance.

# In[34]:


class father:
    def behaviour_father(self):
        return("This is a behaviour of father")


# In[35]:


class mother:
    def behaviour_mother(self):
        return("This is a behaviour of mother")


# In[36]:


class child(father,mother):
    pass


# In[37]:


child_obj = child()


# In[38]:


child_obj.behaviour_father()


# In[39]:


child_obj.behaviour_mother()


# In[40]:


#Question 4


# Getter - It is a method that allows you to access an attribute in a given class.
# Setter - It is a method that allows you to set or mutate the value of an attribute in a class.

# In[80]:


class driving_student:
    def __init__(self,age = 18):
        self.age = age
        
    def get_age(self):
        return self.age
    
    def set_age(self,x):
        self.age = x


# In[81]:


Shahil = driving_student()


# In[82]:


Shahil.age


# In[83]:


Shahil.set_age(23)


# In[84]:


Shahil.get_age()


# In[85]:


#Question 5


# Overriding method allows a class to inherit behaviour from thier super  class and modify it as per requirements.

# In[93]:


class parent:
    def behaviour(self):
        return ('this is parent class')


# In[94]:


class child(parent):
    def behaviour(self):
        return ('this is child class')


# In[95]:


s = child()


# In[96]:


s.behaviour()


# In[ ]:





# In[ ]:




