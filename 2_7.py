# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:37:49 2022

@author: LG
"""

print("Hello AI world_2270005_권지현")

list1 = []
list2 = []
value = 1
for i in range(0, 3) :
  for k in range(0, 4) :
    list1.append(value)
    value += 1
  list2.append(list1)
  list1 = []

for i in range(0, 3) :
  for k in range(0, 4) :
    print("%3d" % list2[i][k], end = " ")
  print("")