#!/usr/bin/env python
# coding: utf-8

# # Zadanie 1 (10 pkt)
#  Za pomoca symulacji Monte Carlo oszacowac 90% przedzial ufnosci dla parametru przy zmiennej X dla regresji liniowej 
# postaci Y=X+2+?, gdzie X~N(0,1) , zas ?~N(0,s) w zaleznosci od parametru s.Prosze przyjac wielkosc próby N=100, 
# zakres parametru s od 0.1 do 2, z odstepem 0.1. Dla kazdej wartosci parametru s powtórzyc symulacje 1000 razy. Wyniki pokazac na wykresie.
# 

# In[1]:

import numpy as np
import scipy.stats as st
import itertools
import matplotlib.pyplot as plt

def simple_():
    oX = [] 
    oY = []
    s = 0.1
    n = 100 #rozmiar wielkosci proby
    
    for n in range(10): #wykonanie 10 prob
        x=st.norm.rvs(loc = 0, scale = 1, size=100) 
        oX.append(x.mean()) #dodanie x
        #print(x.mean())
        for u in range(20): #kazdroazowo dzielone przez 10 aby uzyskas 0.1, 0.2, 0.3 ...
            for j in range(1000): #powtarzanie 1000 razy dla s
                n= st.norm.rvs(loc = 0, scale = (s+u/10)) #nasze ? loc =0 zawsze , scale = s bedziemy zwiekszac o 0.1 kazdroazowo
        oY.append(n.mean() + x.mean() + 2 ) #os y
        #print(n.mean()) 
    
    #aby byla poprawna kolejnosc osi x, y (naturalna)
    lists = sorted(zip(*[oX, oY]))
    new_x, new_y = list(zip(*lists))
    
    plt.plot(new_x,new_y)

simple_()
    
plt.show()



# %%
