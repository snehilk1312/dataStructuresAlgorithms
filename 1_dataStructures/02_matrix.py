#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 05:30:16 2020

@author: atrides
"""


import numpy as np

l=[['mona',14,89,12],['tuea',98,12,34],['weda',23,45,54]]

a = np.array(l)
# print(a)

# accessing values in matrix

#print(a[2])

#[rint(a[2][1])

# adding a row

a = np.append(a,[['sunaaa',1.2329382,2,3]],axis=0)
#print(a)

# adding a column
a = np.insert(a,[4],[[1],[2],[3],[4]],axis=1)
#print(a)


# deleting a row
a = np.delete(a,[2],axis=0)
#print(a)


# deleting a column
a = np.delete(a,[2],axis=1)
#print(a)

# updating a row in matrix
a[1] = ['snehuhhde',1.7464,5,5]
print(a)

# Note: while updating we can see the max size of the corresponding
# element can be what  max size could be corresponding to before the update