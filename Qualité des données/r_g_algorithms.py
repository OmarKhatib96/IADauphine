


from match_merge import Match,Merge


import numpy as np
from distances import *
import pandas as pd
from scipy.spatial import distance

filename="./dataset_b.csv"

data=pd.read_csv(filename)
data=data.drop(columns=['PRODUIT'])
data.head()

r=['CODE_MARQUE','NOM_MARQUE','CA_REF_NATIONALE','CA_NC_NATIONAL']


data=data[r]


I=tuple(data)
print(I)



def g_algorithm(I):#input set of tuples
    I_p=set()#ensemble vide
    while(len(I)!=0):#tant que I n'est pas vide
        t=I.pop()
        if(len(I_p)!=0):
            for  t_p in I_p:
                if(t!=t_p):
                    if Match(t,t_p):
                        t_p_p=Merge(t,t_p)
                        if(t_p_p not in set.union(I,I_p,t)):
                            I.add(t_p_p)
                    I_p.remove(t_p)
        I_p.add(t)
    return I_p





def r_algorithm(I):
    I_p=set()#Ensemble vide
    while(len(I)!=0):
        t=I.pop()
        buddy=None
        if(len(I_p)!=0):
            for t_p in I_p:
                if(Match(t,t_p)):
                    buddy=t_p
                break#exit for
        if buddy==None:
            I_p.add(t)

        else:

            t_p_p=Merge(t,buddy)
            I_p.remove(buddy)
            I.add(t_p_p)
    return I_p







