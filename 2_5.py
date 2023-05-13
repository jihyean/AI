# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:34:59 2022

@author: LG
"""

print("Hello AI world_2270005_권지현")

hap, i = 0,0

for i in range(1,101) :
  if (i % 3 == 0) and (i %7 == 0) :
    continue
  hap += i
  
print("1~100의 합계(3과 7의 베수 제외) : %d" % hap)