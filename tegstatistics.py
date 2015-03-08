# -*- coding: utf-8 -*-
'''
Little script meant to analyse elemental statistical stuff about the 
sequence of dice numbers rolled during a TEG game. The primary goal is
to find out if different playes tend to score differently. I start by 
making a histogram of each player's performance.

@author: sarroyo
'''
import numpy as np
import matplotlib.pyplot as plt


# Data, dice score secuence for each player
Lo=np.array([2, 3, 4, 3, 5, 4, 4, 2, 2, 2, 3, 4, 4, 1, 5, 5, 4, 3, 2, 1, 2, 3, 6, 3, 4, 4, 4, 3, 4, 2, 3, 1, 1, 4, 5, 3, 6, 5, 1, 2, 5, 3, 6, 5, 1, 2, 5, 3, 5, 1, 1, 3, 5, 1, 6, 6, 3, 2, 2, 1, 2, 2, 4, 4, 1, 1, 2, 5, 4, 4, 1, 2, 2, 1])
Lu=np.array([2, 1, 2, 1, 6, 6, 1, 4, 3, 2, 6, 2, 2, 2, 2, 4, 6, 5, 4, 6, 4, 6, 6, 4, 6, 1, 6, 4, 6, 4, 5, 6, 6, 5, 3, 3, 6, 5, 5, 6, 1, 4, 6, 3, 2, 4, 4, 1, 5, 5, 1, 6, 3, 5, 4, 2, 6, 4, 1, 6, 6, 2, 2, 5, 4])
Go=np.array([1, 5, 4, 1, 6, 2, 6, 1, 4, 1, 4, 5, 6, 3, 3, 4, 4, 3, 5, 1, 4, 6, 4, 4, 6, 2, 6, 4, 6, 1, 5, 1, 5, 4, 1, 1, 4, 3, 3, 4, 3, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 2, 4, 1])
Se=np.array([4, 1, 1, 6, 6, 3, 2, 1, 3, 4, 5, 2, 1, 4, 3, 2, 5, 4, 6, 6, 6, 1, 5, 1, 2, 5, 3, 1, 6, 1, 5, 5, 2, 6, 2, 6, 5, 5, 5, 5, 3, 6, 6, 4, 2, 6, 6, 2, 2, 3])
# list of list of data (not arra because different length)
Dat=[[Lo,Lu],[Go,Se]]
# players names
Jugadores=[['Lore','Lu'],['Gon','Seba']]
# compute number of throws of each player
tiradas=[[np.size(Lo),np.size(Lu)],[np.size(Go),np.size(Se)]]
promedio=[[np.average(Lo),np.average(Lu)],[np.average(Go),np.average(Se)]]



def savehistfigure(Dat,Jugadores,tiradas,promedio):
	'''
	Function that plots the histogram for each player.
	'''
	
	xlabels=['', 1, 2, 3, 4, 5, 6, '']# x axis labels
	
	
	fig, axis = plt.subplots(2,2)# create four plots
	bins=np.arange(0.5,7.5,1) # bins edges to compute frequency
	prob=1.0/6.0 # probability if ideal
	
	# loop
	for i in range(2):
		for j in range(2):
			# leyend to be displayed on graph
			txt='%d tiradas\npromedio %1.2f'%(tiradas[i][j],promedio[i][j])
			axis[i,j].set_yticklabels([])
			axis[i,j].set_ylim([0,0.3])
			axis[i,j].set_yticks([])
			axis[i,j].set_xticklabels(xlabels)
			axis[i,j].text(0.3, 0.23, txt)
			axis[i,j].set_title(Jugadores[i][j])
			axis[i,j].plot([0.5,6.5],[prob, prob])
			axis[i,j].hist(
				Dat[i][j], 
				bins=bins, 
				normed=True, 
				histtype='bar', 
				align='mid', 
				rwidth=0.9)
	# once constructed all four histograms, save image
	plt.savefig('histogramas.png')


def comparemodels(Dat,Jugadores):
	'''
	I propose two models for the probability of each dice face.
	Model 0 consists of equal constant probability for each face
	(1/6). Model 1 describes the probability of each face as a
	linear function of the number of the face (to test if some 
	people have greater/lower probability of getting higher 
	scores).
	This function returns the ratio P(Mod1|Data)/P(Mod0|Data) and 
	also graphs the probability distribution of the slope of the 
	linear function.
	'''
	
	# get frequency of appearance of each score
	freq=np.ndarray([2,2,6]) # variable to save feqs
	for i in range(2):
		for j in range(2):
			freq[i,j]=np.histogram(Dat[i][j],6,(0.5,6.5))[0]
	
	atics=20 # Number of intervals to plot a
	a_range=np.linspace(0,7.0/12,atics) # range of posible slopes
	prob_a=np.ndarray([2,2,atics]) # to save prob dist of a
	
	# calculate prob dist of slope for each player
	for i in range(2):
		for j in range(2):
			# evaluate probability at each a
			# function comes out from ...
			prob_a[i,j]=[
				np.sum([ ((l-3.5)*a_range[k]+1.0/6)**freq[i][j]
				 for l in range(1,7)])
				for k in range(atics)]
	
	# now plot
	fig, axis = plt.subplots(2,2)# create four plots
	for i in range(2):
		for j in range(2):
			# leyend to be displayed on graph
#			axis[i,j].set_yticklabels([])
#			axis[i,j].set_ylim([0,0.3])
#			axis[i,j].set_yticks([])
#			axis[i,j].set_xticklabels(xlabels)
#			axis[i,j].text(0.3, 0.23, txt)
			axis[i,j].set_title(Jugadores[i][j])
#			axis[i,j].plot([0.5,6.5],[prob, prob])
			axis[i,j].plot(a_range,prob_a[i][j])
	# once constructed all four histograms, save image
	plt.savefig('aProbdist.png')







comparemodels(Dat,Jugadores)












