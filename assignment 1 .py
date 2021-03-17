#!/usr/bin/env python
# coding: utf-8

# ___
# 
# Mr. Yogesh P Murumkar (Mob. 9657080906)
# 
# https://www.youtube.com/c/yogeshmurumkar
# ___
# # Python Course Exercises 1
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners.

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7**4


# In[ ]:





# ** Split this string:**
# 
#     s = "Hi there Yogesh!"
#     
# **into a list. **

# In[4]:


s = "Hi there Yogesh!"
x=s.split()
print(x)


# In[ ]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[36]:


planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))


# In[ ]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[42]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]


# In[ ]:





# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[18]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[40]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable
#List is mutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[41]:


def domainGet(email):
    print("Your domain is: " + email.split('@')[-1])
email = input("Please enter your email: >")
domainGet(email)


# In[ ]:





# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[37]:


def find_dog(a):
    return 'dog' in a.lower().split()
find_dog("this is a dog")


# In[ ]:





# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[41]:


def countdogs(string):
    count = 0
    for word in string.lower().split():
        if word == 'dog':
            count = count + 1
        print(count)
countdogs("there is dog")


# In[ ]:





# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[39]:


seq = ['soup','dog','salad','cat','great']
list(filter(lambda x:x[0]=='s',seq))


# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[21]:


def caughtspeeding(speed, birthday):
    if birthday:
        s= speed - 5
    else:
        s= speed
    if s<=60:
        print("No ticket")
    elif s>=61 and s<=80:
        print("Small Ticket")
    else:
        print("big ticket")


# In[38]:


caughtspeeding(70,False)


# In[27]:


caughtspeeding(85,False)


# In[ ]:


Question
Given a string print number num by extracting all the
digits from the string as in string
Print negative number if the first character in 
string is '-'
eg.
-123abcd should return -123,abcd456-->456,fdhfh78dsd89--->7889,-56dssd78-->5678


# In[8]:


s=input("Enter the Input > ")
num=''
a=[0,1,2,3,4,5,6,7,8,9]
if s=='':
    print('Enter something > ')
elif s[0] == '-':
    num=num+s[0]
for c in s :
    if c in str(a):
        num=num+c
print(num)


# In[ ]:





# In[ ]:


Q2
WAP to check whether a number is palindrome or not on following conditions.
1. take input number
2. add number and its reverse
3. check that number is palindrome or not,if not then sum and its reverse


# In[15]:


num1 = input('Enter the number')
num2 = int(num1[::-1])
num1 = int(num1)
num3 = num1+num2
num3 = str(num3)
while (int(num3)!=int(num3[::-1])):
    num4 = int(num3[::-1])
    print('Reverse',num4)
    print('number',num3)
    num5 = str(int(num3)+num4)
    if (num5 == num5[::-1]):
        print('palindrome',num5)
        break
    else:
        num3 = num5


# In[ ]:





# In[ ]:


Write a python function to find and display the five 
digit number in which the first digit is two more than 
the second,the second digit is two more than the third,
the fourth digit is two less than the third, and the 
last digit is two more than
the fourth.The sum of the third,fourth and fifth digits
equals the first.The sum of all the digits is 19


# In[6]:


def fivedigitnumber():
   for i in range(9,0,-1):
       first=i
       second = i-2
       third=i-4
       fourth=i-6
       fifth=i-4
       if third+fourth+fifth==first:
           if (first+second+third+fourth+fifth)==19:
               return(int(str(first)+str(second)+str(third)+str(fourth)+str(fifth)))
print(fivedigitnumber())


# # Great job!
