#!/usr/bin/env python
# coding: utf-8

# In[1]:


1 + 1


# In[2]:


2**4


# In[3]:


2*4


# In[5]:


x = 2
y = 3
z = x + y


# In[6]:


z


# In[7]:


x = 'hello'
print (x)


# In[11]:


num = 12
name = 'Sam'
print('My number is: {}, and my name is: {}'.format(num,name))


# In[13]:


age = 36
my_name = "Muhammad Abdul Basit"
print(f"my name is {my_name}, and my age is {age}")


# In[14]:


[1,2,3]


# In[16]:


['hi', 1, [1,2]]


# In[17]:


my_list = ['a','b','c']
my_list.append('d')
my_list


# In[19]:


my_list.insert(2, "m")
my_list


# In[20]:


my_list[0]


# In[21]:


my_list[1]


# In[22]:


my_list[1:]


# In[23]:


my_list[:1]


# In[24]:


my_list[0]="NEW"
my_list


# In[25]:


nest = [1,2,3,[4,5, ['target']]]
nest


# In[26]:


nest[3]


# In[28]:


nest[3][2]


# In[29]:


nest[3][2][0]


# In[30]:


d = {'key1':'item1','key2':'item2'}
d["key1"]


# In[2]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd


# In[5]:



my_dict = {
    "Names" : ["Mohd" , "Asad" , "Zahid" , "Salman"],
    "Marks" : [55,66,77,88],
    "CGPA" : [2.5, 3, 3.2, 3.5]
}
df=pd.DataFrame(my_dict)
df


# In[6]:


True


# In[7]:


False


# In[8]:


t = (1,2,3)
t[0] = 'NEW'


# In[9]:


t[0]


# In[10]:


t[1]


# In[11]:


{1,2,3}


# In[12]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[13]:


1 < 2


# In[14]:


1 > 2


# In[15]:


1 >= 1


# In[16]:


1 <= 4


# In[17]:


1 == 1


# In[18]:


'hi' == 'bye'


# In[19]:


(1 > 2) and (2 < 3)


# In[20]:


(1 > 2) or (2 < 3)


# In[21]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[22]:


(1 == 2) or (2 == 3) or (4 == 4.0)


# In[3]:


if 1 < 2:
    print('Yep!')


# In[4]:


if 1 < 2:
    print('yep!')


# In[6]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[7]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[8]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('last')


# In[14]:


brand = "polo"
price = 1000
if brand == "polo":
    print("You have got a nice brand")
elif price == 1200:
    print("Price is reasonable")
else:
    print("You are out of brand and cash")


# In[15]:


seq = [1,2,3,4,5]
for item in seq:
    print(item)


# In[16]:


for item in seq:
    print('Yep')


# In[17]:


for jelly in seq:
    print(jelly+jelly)


# In[18]:


i = 1
while i <10:
    print('i is: {}' .format(i))
    i = i + 1


# In[19]:


range(5)


# In[20]:


range(1,10)


# In[21]:


for i in range(5):
    print(i)


# In[22]:


for i in range(1,10):
    print(i)


# In[23]:


list(range(5))


# In[24]:


tuple(range(10))


# In[25]:


x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
    print(out)


# In[26]:


[item**2 for item in x]


# In[27]:


[3*i for i in x]


# In[30]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)


# In[31]:


my_func()


# In[32]:


my_func('new param')


# In[33]:


my_func(param1='new param')


# In[34]:


def square(x):
    return x**2


# In[35]:


out = square(2)


# In[36]:


print(out)


# In[37]:


def sum_of_nums(num1, num2):
    new_num = num1 + num2
    return new_num


# In[38]:


sum_of_nums(2,3)


# In[39]:


def times2(var):
    return var*2


# In[40]:


times2(2)


# In[41]:


sqar = lambda var: var*2
print(sqar)


# In[43]:


seq = [1,2,3,4,5]
map(times2,seq)


# In[44]:


list(map(times2,seq))


# In[45]:


list(map(lambda var: var*2,seq))


# In[47]:


fil = filter(lambda item: item%2 == 0,seq)
fil


# In[48]:


list(filter(lambda item: item%2 == 0,seq))


# In[49]:


st = 'hello my name is Sam'


# In[50]:


st.lower()


# In[51]:


st.upper()


# In[52]:


st.split()


# In[53]:


tweet = 'Go Sports! #Sports'


# In[54]:


tweet.split('#')


# In[55]:


tweet.split('#')[1]


# In[56]:


email = "ab.muhammad3112@gmail.com"


# In[57]:


email.split()


# In[58]:


email.split('@')


# In[62]:


d = {'key1': 'item1', 'key2': 'item2'}


# In[63]:


d.keys()


# In[64]:


d.items()


# In[65]:


lst = [1,2,3]


# In[66]:


lst.pop()


# In[67]:


lst


# In[68]:


'x' in [1,2,3]


# In[69]:


'x' in ['x','y','z']


# In[72]:


print(2+3)


# In[ ]:




