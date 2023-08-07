# -*- coding: utf-8 -*-
'''
The code I created for the MATH40A final project
recreating teh results of the Logic of Animal Conflict Paper '''
import animal
import pandas as pd
from random import random

def simulation(a1, a2):
    win = 60 #win value
    n = 0   #total payoff across sims
    t = 20000  #numeber of sims
    for i in range(t):

        #alternate between who goes first and second
        if i != 0:
            temp = a1
            a1 = a2
            a2 = temp
        
        a1turns = []
        a2turns = []
        
        cont = True
        
        #turns while one has not retreated
        while cont :
            a1.move(a2, a1turns, a2turns)
            if a1turns[len(a1turns) - 1] == 'R':
                cont = False
            else:
                a2.move(a1, a2turns, a1turns)
                if (a2turns[len(a2turns) - 1] == 'R'):
                    cont = False
                    
        #winner recieves payoff    
        if a1turns[len(a1turns) - 1] == 'R':
            a2.gain += win 
        else:
            a1.gain += win
            
        #bonus for uninjured    
        if len(a1turns) <= 1:
            if a1.injured == False:
                a1.gain += 20
            if a2.injured == False:
                a2.gain += 20
                
        #bonus for short game
        elif len(a1turns) <= 22:
            if a1.injured == False:
                a1.gain += 20 - (len(a1turns)-1 )
            if a2.injured == False:
                a2.gain += 20 - (len(a1turns)-1 )
                
        #record gain for animal we are examining
        if i%2 == 1:
            n += a2.gain
        else:    
            n += a1.gain
        
        a1.clear()
        a2.clear()
    mean = n / t
    return mean

def main():
    '''performing the simulations for each matchup
    returns a dataframe formatted in the same way as the table
    in the paper'''
    animals1 = [animal.mouse(), animal.hawk(), animal.bully(), animal.retaliator(), animal.p_r() ]
    animals2 = [animal.mouse(), animal.hawk(), animal.bully(), animal.retaliator(), animal.p_r() ]    
    pay_list = [[0 for i in range(5)] for j in range(5)]
    
    for i in range(5):
        for j in range(5):
            pay_list[i][j] = simulation(animals1[i],animals2[j])
                    
    payoff = {'Mouse':pay_list[0], 'Hawk':pay_list[1],
              'Bully':pay_list[2], 'Retaliator':pay_list[3],
              'Prober-Retaliator':pay_list[4]}       
    
    #formatting dataframe like the paper
    df = pd.DataFrame(data=payoff)
    df2 = df.rename(index={0:'Mouse', 1:'Hawk', 2:'Bully',3:'Retaliator', 4:'Prober-Retaliator'})
    df2_transposed = df2.T
    return df2_transposed


df = main()       