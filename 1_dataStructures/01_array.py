#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 05:11:22 2020

@author: atrides
"""

from array import array

# creating an array
array1 = array('i', [10,20,30,40,50])

for i in array1:
    print(i)


# accessing array element
print(array1[2])

# insertion operation
array1.insert(1,60)
array1.insert(3,89)
array1.insert(-1,20)

# deletion operation
array1.remove(20)

# search operation
print(array1.index(20))

# update operation
array1[2] = 76

print(array1)