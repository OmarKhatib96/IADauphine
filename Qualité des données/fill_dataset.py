import csv
import random

from match_merge import *



marques=["Schneider","LeGrand","Lejeune","DistElectrique","Marchais","Leclerc_electrique","Phillips_France"]
filename="dataset(1)"
nbr_lignes=100
CA_min=100.5
CA_max=1000.6

def fill_data(my_file):

    with open(my_file, 'w', newline='') as csvfile:
        from math import floor
        datawriter = csv.writer(csvfile, delimiter=',')
        datawriter.writerow(["PRODUIT","CODE_MARQUE","NOM_MARQUE","CA_REF_NATIONALE","CA_NC_NATIONAL","CA_REF_CONNECT","CA_NC_CONNECT","DATE_DU_DERNIER_TARIF","NBR_MARQUES_REFERENTEES","NBR_OFFRES_HORS_OFFRES","TOUT_PARTOUT","MONTANT_OFFRE_100_957","MONTANT_OFFRE_200_957","MONTANT_OFFRE_300_957","MONTANT_OFFRE_100_612"])

        for i in range(0,nbr_lignes-1):
            my_index=get_code_marque(i)
            nbr_referencees=get_nbr_referencees()
            nbr_NC=13-nbr_referencees
            montant1= floor(random.uniform(1, 20))
            montant2= floor(random.uniform(1, 20))
            montant3= floor(random.uniform(1, 20))
            montant4= floor(random.uniform(1, 20))
            datawriter.writerow([i+1,my_index+1,marques[my_index] ,get_random_CA(),get_random_CA(),get_random_CA(),get_random_CA(),get_random_date(random.randint(2012,2020)),nbr_referencees,nbr_NC,nbr_referencees+nbr_NC,montant1,montant2,montant3,montant4])


def get_code_marque(index):
    my_index=random.randint(0,len(marques)-1)
    return my_index


def get_random_CA():
    from math import floor
    return int(random.uniform(CA_min, CA_max))



def get_nbr_referencees():
    return random.randint(0,13)





# import modules
import random
import datetime
def get_random_date(year):

    try:
        date= str(datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y'))
        return date[0:11]
    except ValueError:
        get_random_date(year)






fill_data("dataset_b.csv")