#!/usr/bin/env python
# coding: utf-8

# In[1]:


def odd():
    a = [0,1,1]
    while len(a) != 500:
        a.append(a[-1]+a[-2])
    line = ''
    for i in range(len(a)):
        line += str(a[i])
    return line

line = odd()

def hash1(a):
    m = 1
    alphabet = 10
    #0 - 0, 1 - 1 и т.д
    a = str(a)
    h = int(a[0])*10**1+int(a[1]*10**0)
    return h

def rabin_karp(a):
    k = 0
    topp = []
    for j in range(10,100):
        for i in range(len(a)-1):
            if hash1(j) == hash1(a[i]+a[i+1]):
                k += 1
        else:
            topp.append(k)
            k = 0
    return max(topp), topp.index(max(topp))+10

print(rabin_karp(line))


# In[ ]:




