# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:59:49 2022

@author: thomthawee
"""

#Class 1
"""
#Just Note how to use repo
#1. create a repo (via Github desktop)
#2. Clone locally
#3. .py and save in the cloned folder
#4. commit/push
#5. Share with member (only in website)

#Fork
#Duplicate the repo and can develop by yourself(just copy)


#Pull request
#Got our duplicate work back to main repo
End of class 1
"""

#Week 2 , Class 1 : data type
"""
First import datetime <- python does not have basic datatype that can be used with date directly (not intended to use with data analysis)


***Data Type***

-Numeric
    - Integer
    - Float
    
-Boolean : T and F *** need '==' to prove T or F

-string : world that actually assign with '',"" and can use + operator to merge
*** string.method/attribute()
*** String Formatting
use .string(var_name) <- look at lecture (line 67-75)
*We can use it to create more string repeatedly*

-List : group of elements created by [] 
    - command my_list[start:stop:strp]
*Close on the left open on the right [index : count]*

-Tuple : () <- unchangable

-Dictionaries : {key1 : value , key2 : value}
    -Python only indexs by position
    -want to indexs by names <- use dictionaries
    
-Date times : a = datetime.datetime(year,month,day)


**Terminology***

class  = blue-print (instruct you what you should have)
instance = object e.g. garage
*We can create many houses from 1 blue print = we can create many instance from 1 class*

check datatype = print(type(a))
check length = print(len(a))
x =+ number <- it help to add the value from existing variable (x)
**use when you loop x+=1 (syntactic sugar)


***Method***

.upper() <- All Upper Letter
.capitalize() <- Capital Letter
.strip() <- Find the first letter to be the first word                                             

"""
