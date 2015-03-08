# -*- coding: utf-8 -*-
'''
Para analizar las distribuciones de las tiradas de dados de cada jugadoren tres rondas de TEG. Para la próxima tomar en cuenta si se ataca o se defiende, quien se enfrenta a quien, agrupar las tiradas, etc. Por ahora nos conformamos con un histograma y el valor medio.

@author: sarroyo
'''
import numpy as np
import matplotlib.pyplot as plt


# cargo los datos
Lo=np.array([2, 3, 4, 3, 5, 4, 4, 2, 2, 2, 3, 4, 4, 1, 5, 5, 4, 3, 2, 1, 2, 3, 6, 3, 4, 4, 4, 3, 4, 2, 3, 1, 1, 4, 5, 3, 6, 5, 1, 2, 5, 3, 6, 5, 1, 2, 5, 3, 5, 1, 1, 3, 5, 1, 6, 6, 3, 2, 2, 1, 2, 2, 4, 4, 1, 1, 2, 5, 4, 4, 1, 2, 2, 1])
Lu=np.array([2, 1, 2, 1, 6, 6, 1, 4, 3, 2, 6, 2, 2, 2, 2, 4, 6, 5, 4, 6, 4, 6, 6, 4, 6, 1, 6, 4, 6, 4, 5, 6, 6, 5, 3, 3, 6, 5, 5, 6, 1, 4, 6, 3, 2, 4, 4, 1, 5, 5, 1, 6, 3, 5, 4, 2, 6, 4, 1, 6, 6, 2, 2, 5, 4])
Go=np.array([1, 5, 4, 1, 6, 2, 6, 1, 4, 1, 4, 5, 6, 3, 3, 4, 4, 3, 5, 1, 4, 6, 4, 4, 6, 2, 6, 4, 6, 1, 5, 1, 5, 4, 1, 1, 4, 3, 3, 4, 3, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 2, 4, 1])
Se=np.array([4, 1, 1, 6, 6, 3, 2, 1, 3, 4, 5, 2, 1, 4, 3, 2, 5, 4, 6, 6, 6, 1, 5, 1, 2, 5, 3, 1, 6, 1, 5, 5, 2, 6, 2, 6, 5, 5, 5, 5, 3, 6, 6, 4, 2, 6, 6, 2, 2, 3])
# los pongo en una lista (tienen distinto largo)
Dat=[[Lo,Lu],[Go,Se]]
Jugadores=[['Lore','Lu'],['Gon','Seba']]
tiradas=[[np.size(Lo),np.size(Lu)],[np.size(Go),np.size(Se)]]
promedio=[[np.average(Lo),np.average(Lu)],[np.average(Go),np.average(Se)]]




fig, axis = plt.subplots(2,2)
bins=np.arange(0.5,7.5,1)
prob=1.0/6.0 # prob unif dist
for i in range(2):
	for j in range(2):
		axis[i,j].set_yticklabels([])
		axis[i,j].set_ylim([0,0.3])
		axis[i,j].set_yticks([])
		axis[i,j].set_xticklabels(['',1,2,3,4,5,6,''])
		axis[i,j].text(0.3, 0.23, 
			'%d tiradas\npromedio %1.2f'%(tiradas[i][j],promedio[i][j]))
		axis[i,j].set_title(Jugadores[i][j])
		axis[i,j].plot([0.5,6.5],[prob, prob])
		axis[i,j].hist(
			Dat[i][j], 
			bins=bins, 
			normed=True, 
			histtype='bar', 
			align='mid', 
			rwidth=0.9)

plt.savefig('histogramas.png')























