'''Pour chaque machine a, 
on génère q?(a) en tirant un échantillon 
d’une distribution normale de moyenne 1 et de variance 1 (N(0,1)). 
à chaque fois qu’on joue à la machine a, on tire un échantillon 
en suivant une loi normale de moyenne q?(a) et de variance 1. 
on utilise un algorithme en choisissant 1000 fois une machine.
 ë un "run" pour obtenir des informations plus ﬁables, on répète 2000 "runs"
  (on tire au sort les valeurs q?, puis on choisit 1000 fois une machine)
'''
from random import gauss

nbr_jetons=10000
nbr_machines=10


def random_expectancies():
    Q=[]
    for i in range(0,nbr_machines):
        Q.append(gauss(1,1))
    return Q

def game_playing(machine_number,runs):
    expectancies=random_expectancies()
    gains=[0]
    for run in range(0,runs):
        gains.append(gauss(expectancies[machine_number],1))
    return gains

    
def launch_simulation(n_times,runs):

    simulation_results=[]
    total_simulation=[]
    for machine in range(0,nbr_machines):
            for i in range(0,n_times):
                simulation_results.append(np.average(game_playing(machine,runs)))
            total_simulation.append(simulation_results)
    return (total_simulation)

from random import uniform
from random import randint
import numpy as np

def k_bandits(epsilon):
    final_results=[]
    outcome=uniform(0, 1)
    total_simulation=np.array(launch_simulation(nbr_jetons,2))

    for iteration in range(0,nbr_jetons):

        if outcome<=epsilon:
            index_machine=np.argmax(total_simulation[:,0])
        
        else:
            index_machine=randint(1,nbr_machines)-1

        final_results.append(total_simulation[index_machine][iteration])

    return final_results



final_results=k_bandits(0.01)

import matplotlib.pyplot as plt

plt.plot(final_results)
plt.ylabel('Average gains')
plt.show()





