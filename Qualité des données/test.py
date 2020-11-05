from distances import *
import pandas as pd
from scipy.spatial import distance

filename="dataset_b.csv"

data=pd.read_csv(filename)
data=data.drop(columns=['PRODUIT'])
data.head()

r=['CODE_MARQUE','NOM_MARQUE','CA_REF_NATIONALE','CA_NC_NATIONAL']


#ata=data[r]

'''
I=tuple(data)
print(I)
'''