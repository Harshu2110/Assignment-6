#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1)What are escape characters, and how do you use them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:


Ans: Escape characters are special characters that are used to represent certain characters in strings or text that would otherwise be difficult or impossible to type directly.
    
    Some examples of escape characters include:

\n: represents a new line character
\t: represents a tab character


# In[3]:


print("This is a new line.\n This is a tab.\t")


# In[ ]:


get_ipython().set_next_input('2. What do the escape characters n and t stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


Ans:  \n: represents a new line character
\t: represents a tab character


# In[ ]:


get_ipython().set_next_input('3. What is the way to include backslash characters in a string');get_ipython().run_line_magic('pinfo', 'string')


# In[ ]:


Ans : To include a backslash character in a string, we need to use the backslash character () as an escape character before the backslash we want to include. This tells the interpreter to treat the backslash as a literal character, rather than as the start of an escape sequence.


# In[ ]:


4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
get_ipython().set_next_input("word Howl's not escaped a problem");get_ipython().run_line_magic('pinfo', 'problem')


# In[ ]:


Ans : The reason why the single quote character in the word "Howl's" in the string "Howl's Moving Castle" is not causing a problem is because the string itself is enclosed in double quotes, not single quotes.


# In[ ]:


get_ipython().set_next_input("5. How do you write a string of newlines if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')


# In[ ]:


Ans: We can use triple quote string, Python allows us to define a string using triple-quotes, which can span multiple lines. 


# In[5]:


newline =""" 


"""


# In[ ]:


get_ipython().set_next_input('6. What are the values of the given expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]


# In[9]:


'Hello, world!'[1]


# In[10]:


'Hello, world!'[0:5]


# In[11]:


'Hello, world!'[:5]


# In[12]:


'Hello, world!'[3:]


# In[ ]:


get_ipython().set_next_input('7. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()


# In[13]:


'Hello'.upper()


# In[14]:


'Hello'.upper().isupper()


# In[15]:


'Hello'.upper().lower()


# In[ ]:


get_ipython().set_next_input('8. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())


# In[16]:


'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())


# In[ ]:


get_ipython().set_next_input('9. What are the methods for right-justifying, left-justifying, and centering a string');get_ipython().run_line_magic('pinfo', 'string')


# In[21]:


string = "hello"
width = 20
justified_string = string.rjust(width)
print(justified_string)


# In[24]:


string = "hello"
width = 20
justified_string = string.ljust(width)
print(justified_string)


# In[25]:


string = "hello"
width = 20
justified_string = string.center(width)
print(justified_string)


# In[ ]:


get_ipython().set_next_input('10. What is the best way to remove whitespace characters from the start or end');get_ipython().run_line_magic('pinfo', 'end')


# In[ ]:


In Python, we can use the strip() method to remove whitespace characters from the start or end of a string. 


# In[ ]:





# In[ ]:




