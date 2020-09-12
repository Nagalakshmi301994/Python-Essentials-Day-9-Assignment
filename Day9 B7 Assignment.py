#!/usr/bin/env python
# coding: utf-8

# # Write a python Function for finding is a given number prime or not and do Unit Testing on it using PyLint and Unittest Library.

# In[2]:


get_ipython().system(' pip install pylint')


# In[3]:


get_ipython().run_cell_magic('writefile', 'prime.py', "'''\nIt is  a prime number\n'''\ndef isprime(num):\n    '''\n    It is\n    '''\n    if num in(0, 1):\n        return False\n    for prime in range(2, num-1):\n        if num % prime == 0:\n            return False\n        return True")


# In[4]:


get_ipython().system(' pylint prime.py')


# In[5]:


import prime
prime.isprime(199)


# # USING UNIT TEST

# In[6]:


get_ipython().run_cell_magic('writefile', 'newprime.py', '\nimport unittest\nimport prime\n\nclass primenumber(unittest.TestCase):\n    def testprime(self):\n        Number = 32\n        result = prime.isprime(Number)\n        self.assertEquals(result, False)\n\n        \n    def testprimenum(self):\n        Num = 199\n        res = prime.isprime(Num)\n        self.assertEquals(res, True)\n\n        \n        \nif __name__ == "__main__":\n    unittest.main()')


# In[7]:


get_ipython().system(' python newprime.py')


# # Make a small generator program for returning armstrong numbers in between 1-1000 in a generator object.

# In[8]:


lst = list(range(1,1000))


# In[9]:


print(lst)


# In[10]:


def getArmstrongNumGen(lst):
    for num in lst:
        order=len(str(num))
        temp=num
        sum=0
        while temp >0:
            digit=temp%10
            sum=sum+digit**order
            temp=temp//10
        if sum==num:
             yield num


# In[11]:


print(list(getArmstrongNumGen(lst)))


# In[ ]:




