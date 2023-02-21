#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def odd():
    a = [0,1,1]
    while len(a) != 500:
        a.append(a[-1]+a[-2])
    line = ''
    for i in range(len(a)):
        line += str(a[i])
    return line

line = odd()

pattern = '71'
def finder_boira_muera(string, pattern):
    def if_find(pattern, pattern_lines):
        for i in range(len(pattern)-1, -1, -1):
            if pattern[i] != pattern_lines[i]:
                return False
        return True

    step = len(pattern)
    count = 0
    while step <= len(string):
        
        if if_find(pattern, string[step-len(pattern):step:]):
            count += 1
            step += 1
        else:
            new_step = 0
            for i in range(len(pattern)-2, -1, -1):
                if string[step - 1] == pattern[i]:
                    new_step = (len(pattern) - i) - 1
                    break
                else:
                    new_step += 1
            step += new_step
            if len(pattern) == 1:
                step += 1
    return count

print(finder_boira_muera(line,pattern))l

