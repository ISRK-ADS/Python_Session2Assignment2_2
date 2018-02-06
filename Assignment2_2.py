# -*- coding: utf-8 -*-
""" Created on Sat Feb  3 20:33:51 2018
@author: krishna.i
Assignment 2.2: Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

starval= int(input("Enter No. of Stars: "))

if(starval > 0):
    tempnum = 1
    while tempnum <= starval :
        i=1
        while i <=tempnum :
            print("*",sep=' ',end=' ')
            i=i+1
        print("",end='\n')
        tempnum = tempnum + 1
    
    tempnum=tempnum - 2
    
    while tempnum >=1:
        j=tempnum
        while j >=1:
            print("*",sep=' ',end=' ')
            j=j-1
        print("",end='\n')
        tempnum=tempnum-1
        
# End of the code