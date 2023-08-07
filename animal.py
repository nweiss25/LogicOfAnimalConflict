# -*- coding: utf-8 -*-


from random import random
class animal:
    def __init__(self):
        self.injured = False
        self.gain = 0
        self.injchance = 0.10
        
    def move(self,L1, L2):       #L1 is own array L2 is opponent
        return 
    def conventional(self,A2, L1):
        L1.append('C')
        
    def dangerous(self,A2, L1):
        L1.append('D')
        if isinstance(A2, mouse):
            pass
        elif random() < self.injchance:
            A2.nowInjured() 
        else:
            A2.gain -= 2
            
        
    def retreat(self,A2, L1):
        L1.append('R')
        
    def nowInjured(self):
        self.injured = True
        self.gain -= 100

    def clear(self):
        self.injured = False
        self.gain = 0
        
        
class mouse(animal):
    def __init__(self):
        self.injured = False
        self.gain = 0
        self.injchance = 0.10
        self.maxturn = 25
        
    def move(self,A2,L1, L2):
        if len(L1) >= self.maxturn:
            self.retreat(A2,L1)
        elif len(L2) == 0:
            self.conventional(A2, L1)
        elif L2[len(L2) -1] == 'D':
            self.retreat(A2,L1)
        else:
            self.conventional(A2, L1)
        
class hawk(animal):
    
    def move(self,A2,L1, L2):
        if self.injured == True:
            self.retreat(A2, L1)
        else:
            self.dangerous(A2, L1)
            
class bully(animal):
    
    def __init__(self):
        self.injured = False
        self.gain = 0
        self.d_count = 0
        self.injchance = 0.10
        
    def move(self, A2, L1, L2):
        if len(L2) == 0:
            self.dangerous(A2, L1)
        elif self.injured == True:
            self.retreat(A2, L1)
        elif L2[len(L2) -1] == 'C':
            self.dangerous(A2, L1)
        elif L2[len(L2) -1] == 'D':
            self.d_count += 1
            if self.d_count >= 2:
                self.retreat(A2, L1)
            else:
                self.conventional(A2, L1)
            
class retaliator(animal): 
    #always retaliates in this model
    def __init__(self):
        self.injured = False
        self.gain = 0
        self.injchance = 0.10
        self.maxturn = 25    

    def move(self, A2, L1, L2):
        if len(L2) == 0:
            self.conventional(A2, L1)
        elif self.injured == True:
            self.retreat(A2, L1)
        elif len(L1) >= self.maxturn:
            self.retreat(A2, L1)
        elif L2[len(L2) -1] == 'C':
            self.conventional(A2, L1)
        else:
            self.dangerous(A2, L1)
            
class p_r(animal):
    def __init__(self):
        self.injured = False
        self.gain = 0
        self.injchance = 0.10
        self.maxturn = 25  
        self.struckFirst = False
        
    def move(self, A2, L1, L2):
        
        if len(L2) == 0:
            if random() < 0.05:
                self.struckFirst = True
                self.dangerous(A2, L1)
            else:
                self.conventional(A2, L1)
        elif len(L1) >= self.maxturn:
            self.retreat(A2,L1)
        elif self.injured == True:
            self.retreat(A2, L1)
        elif L2[len(L2)-1] == 'C':
            if random() < 0.05:
                self.struckFirst = True
                self.dangerous(A2, L1)
            else:
                self.conventional(A2, L1)
        elif self.struckFirst == False and L2[len(L2)-1] == 'D':
            self.dangerous(A2, L1)
            
        elif self.struckFirst == True and L2[len(L2)-1] == 'D':
            self.conventional(A2, L1)
            self.struckFirst = False
        elif self.struckFirst == True and L2[len(L2)-1] == 'C':
            self.dangerous(A2, L1)
        
            
        """
        if len(L2) == 0:
            if random() < 0.05:
                self.dangerous(A2, L1)
            else:
                self.conventional(A2, L1)
        elif len(L1) >= self.maxturn:
            self.retreat(A2,L1)
        elif self.injured == True:
            self.retreat(A2, L1)
        elif L2[len(L2)-1] == 'C':
            if random() < 0.05:
                self.dangerous(A2, L1)
            else:
                self.conventional(A2, L1)
        elif len(L1) == 0 and L2[len(L2)-1] == 'D':
            self.dangerous(A2, L1)
            
        elif L1[len(L1)-1] == 'D' and L2[len(L2)-1] == 'D':
            self.conventional(A2, L1)
        elif L1[len(L1)-1] == 'D' and L2[len(L2)-1] == 'C':
            self.dangerous(A2, L1)
        else:
            self.dangerous(A2, L1)
         """