#!/usr/bin/env python
# coding: utf-8

# In[3]:


op = '' # defining variable op
clmns = [] # defining list clmns
def shellfunction(filename, clmns, op): # defining function with 3 inputs
    import pandas as pd # importing pandas
    import seaborn as sns # importing seaborn for plotting
    cl = [] # making an empty list
    clmns = cl # making the empty list equal to clmns
    print('age = 0, sex = 1\nchest pain = 2, resting blood pressure = 3\ncholesterol = 4, fasting blood sugar = 5\nresting ECG = 6, max heart rate = 7\nexercise induced angina = 8, ST depression induced by excercise = 9\nslope of the peak exercise ST segment = 10\nnumber of major vessels colored by flourosopy = 11\nthal = 12, target = 13')
    print('\n') # providing a key
    for i in range(0, 2): # making a for loop where the user can input what elements they want to use
        print("Enter number corresponding to desired element to be plotted")
        item = int(input()) 
        cl.append(item) # appending user input to the empty list made earlier
    x, y = cl # setting up assert statement
    assert x != y, 'Please input different values' # using assert statement to ensure differnt values are used
    print('\n')
    df = pd.read_csv(filename, usecols = clmns) # importing file and designating columns to use from pandas
    op = str(input("What operation would you like to run on this data?:\nAverage(A), Maximum(MX), Minimum(MN), Standard Deviation(STD)\nType A, MX, MN, or STD: "))
    print('\n') # providing instructions for the user
    if op == "A" or op == "a": # set up if, elif, else statements to take on use inputs
        avg = df.mean(axis=0) # average function
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True) #plotting using seaborn
        print(avg)
    elif op == "MX" or op == "mx":
        mx = df.max(axis=0) # max function
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(mx)
    elif op == "MN" or op == "mn":
        mn = df.min(axis=0) # min function
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(mn)
    elif op == "STD" or op == "std":
        stdev = df.std(axis=0) # standard deviation function
        v1, v2 = df
        sns.lmplot(v1, v2, data=df,fit_reg=True)
        print(stdev)
    else:
        print("Invalid Input")


# In[4]:


shellfunction('heart.csv', clmns, op)


# In[ ]:




