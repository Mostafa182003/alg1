#!/usr/bin/env python
# coding: utf-8

# In[3]:


def odd():
    a = [0,1,1]
    while len(a) != 500:
        a.append(a[-1]+a[-2])
    line = ''
    for i in range(len(a)):
        line += str(a[i])
    return line


a = odd()
def naive(a):
    k = 0
    topp = []
    for j in range(10,100):
        for i in range(len(a)-1):
            if str(j) == a[i]+a[i+1]:
                k += 1
        else:
            topp.append(k)
            k = 0
    return max(topp), topp.index(max(topp))+10
print(naive(a))
print(a)


# In[ ]:




