# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:32:13 2022

@author: nweis
"""

import animal
from random import random

win = 60
n = 0
t = 20000

for i in range(t):
    
    a1 = animal.p_r()
    a2 = animal.p_r()
    
    
    #alternate between who goes first and second
    if i % 2 == 1:
        temp = a1
        a1 = a2
        a2 = temp
    
    a1turns = []
    a2turns = []
    
    cont = True
    
    while cont :
        a1.move(a2, a1turns, a2turns)
        if a1turns[len(a1turns) - 1] == 'R':
            cont = False
        else:
            a2.move(a1, a2turns, a1turns)
            if (a2turns[len(a2turns) - 1] == 'R'):
                cont = False
        
    if a1turns[len(a1turns) - 1] == 'R':
        a2.gain += win 
    else:
        a1.gain += win
    if len(a1turns) <= 1:
        if a1.injured == False:
            a1.gain += 20
        if a2.injured == False:
            a2.gain += 20
    elif len(a1turns) <= 22:
        if a1.injured == False:
            a1.gain += 20 - (len(a1turns)-1 )
        if a2.injured == False:
            a2.gain += 20 - (len(a1turns)-1 )
    
    if i%2 == 1:
        n += a2.gain
    else:    
        n += a1.gain
    

mean = n / t
print(n, mean)
#print(a1.gain, a2.gain,a1turns, end=("\n"))
#print(a2turns)