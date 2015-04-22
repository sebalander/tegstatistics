# -*- coding: utf-8 -*-
'''
Little script meant to analyse elemental statistical stuff about the 
sequence of dice numbers rolled during a TEG game. The primary goal is
to find out if different playes tend to score differently. I start by 
making a histogram of each player's performance.

Part of the code in the function savehistfigure is adapted from the code posted as an answer in Stack Overflow. The lines that were remixed from the original code have been properly indicated.The question was made by user bioslime on Aug 2 '12 at 9:39. The code was originally posted in the answer by user imsc on Aug 2 '12 at 10:37.

Question page: http://stackoverflow.com/questions/11774822/matplotlib-histogram-with-errorbars
User bioslime profile page: http://stackoverflow.com/users/1565662/bioslime
User imsc profile page: http://stackoverflow.com/users/302369/imsc

@author: sarroyo
'''
import numpy as np
import matplotlib.pyplot as plt


# Data, dice score secuence for each player
Lo=np.array([2, 3, 4, 3, 5, 4, 4, 2, 2, 2, 3, 4, 4, 1, 5, 5, 4, 3, 2, 1, 2, 3, 6, 3, 4, 4, 4, 3, 4, 2, 3, 1, 1, 4, 5, 3, 6, 5, 1, 2, 5, 3, 6, 5, 1, 2, 5, 3, 5, 1, 1, 3, 5, 1, 6, 6, 3, 2, 2, 1, 2, 2, 4, 4, 1, 1, 2, 5, 4, 4, 1, 2, 2, 1])
Lu=np.array([2, 1, 2, 1, 6, 6, 1, 4, 3, 2, 6, 2, 2, 2, 2, 4, 6, 5, 4, 6, 4, 6, 6, 4, 6, 1, 6, 4, 6, 4, 5, 6, 6, 5, 3, 3, 6, 5, 5, 6, 1, 4, 6, 3, 2, 4, 4, 1, 5, 5, 1, 6, 3, 5, 4, 2, 6, 4, 1, 6, 6, 2, 2, 5, 4])
Go=np.array([1, 5, 4, 1, 6, 2, 6, 1, 4, 1, 4, 5, 6, 3, 3, 4, 4, 3, 5, 1, 4, 6, 4, 4, 6, 2, 6, 4, 6, 1, 5, 1, 5, 4, 1, 1, 4, 3, 3, 4, 3, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 2, 4, 1])
Se=np.array([4, 1, 1, 6, 6, 3, 2, 1, 3, 4, 5, 2, 1, 4, 3, 2, 5, 4, 6, 6, 6, 1, 5, 1, 2, 5, 3, 1, 6, 1, 5, 5, 2, 6, 2, 6, 5, 5, 5, 5, 3, 6, 6, 4, 2, 6, 6, 2, 2, 3])
# list of data vectors (not array because of different length)
Dat=[[Lo,Lu],[Go,Se]]
# players names
Jugadores=[['Lore','Lu'],['Gon','Seba']]




def savehistfigure(Dat,Jugadores):
  '''
  Function that plots the histogram for each player.
  '''
  
  # compute number of throws of each player
  tiradas=[[np.size(Lo),np.size(Lu)],[np.size(Go),np.size(Se)]]
  # average score
  promedio=[[np.average(Lo),np.average(Lu)],
    [np.average(Go),np.average(Se)]]
  
  
  
  xlabels=['', 1, 2, 3, 4, 5, 6, '']# x axis labels
  
  
  fig, axis = plt.subplots(2,2)# create four plots
  bins=np.arange(0.5,7.5,1) # bins edges to compute frequency
  prob=1.0/6.0 # probability if ideal
  
  # loop
  for i in range(2):
    for j in range(2):
      print 'plotting %d %d'%(i,j)
      # leyend to be displayed on graph
      txt='%d tiradas\npromedio %1.2f'%(tiradas[i][j],promedio[i][j])
      axis[i,j].set_yticks([0,1/6.0])
      axis[i,j].set_yticklabels(['0','1/6'])
      axis[i,j].set_ylim([0,0.3])
      axis[i,j].set_yticks([])
      axis[i,j].set_xticklabels(xlabels)
      axis[i,j].text(0.3, 0.23, txt)
      axis[i,j].set_title(Jugadores[i][j])
      axis[i,j].plot([0.5,6.5],[prob, prob])
      
      
      ### Code attributed to user imsc in an answer to user bioslime's
      ### question in Stack Overflow, starts on this line until the line
      ### appropiately indicated.
      # compute histogram
      y,bin_edges=np.histogram(
        Dat[i][j],
        bins=bins, 
        normed=False)
        
      # compute center of bins
      bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])
      
      # now plot bars with error bars
      axis[i,j].bar(
        bin_centers,
        y*1.0/tiradas[i][j],
        yerr = y**0.5/tiradas[i][j])
#        marker = '.')
#        drawstyle = 'steps-mid-')
      
      ### End of the code attributed to user imsc in an answer to user
      ### bioslime's question in Stack Overflow.
      
#      axis[i,j].hist(
#        Dat[i][j], 
#        bins=bins, 
#        normed=True, 
#        histtype='bar', 
#        align='mid', 
#        rwidth=0.9)
      print 'plotting %d %d'%(i,j)
  # once constructed all four histograms, save image
  plt.savefig('histogramas2.png')
  plt.show()






def comparemodels01(Dat,Jugadores):
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
  
  freq=np.ndarray([2,2,6]) # variable to save feqs
  atics=200 # Number of intervals to plot slope
  a_range=np.linspace(-1.0/15,1.0/15,atics) # range of posible slopes
  prob_a=np.ndarray([2,2,atics]) # to save prob dist of a
  
  p6=1.0/6 # probability if uniform
  
  # calculate prob dist of data given slope for each player 
  #do with respect to prob of data given model 0 to take results 
  #of each player to same level. They differ in number of throws.
  for i in range(2):
    for j in range(2):
      # get frequency of appearance of each score
      freq[i,j]=np.histogram(Dat[i][j],6,(0.5,6.5))[0]
      prob_model0=1.0/(6**np.sum(freq[i,j]))
      # evaluate probability of data given slope
      # function comes from ...
      prob_a[i,j]=[ 
        np.prod(    [
           ((l-3.5)*a_range[k]+p6) 
           for l in range(1,7)]
             **freq[i][j]   )
        for k in range(atics)] /  prob_model0#[i,j]
        #don't know how to do the normalization more 
        #efficiently...
  
  
  
#  prob_model0=1.0/(6**np.sum(freq,2)) # (1/6)**(Number of rolls)
  #probability of data given model 1 (integrated over slope values) 
  #with respect to probability of data given Model 0.
  d_a=1.0/15/atics # columns width, useful for integration
  mod1_mod0=np.sum(prob_a,2)*d_a#/  prob_model0
  
  print mod1_mod0# , prob_model0
  
  # now plot
  fig, axis = plt.subplots(2,2)# create four plots
  probmax = np.max(np.max(np.max(prob_a))) # limit of y axis
  for i in range(2):
    for j in range(2):
      # leyend to be displayed on graph
#      axis[i,j].set_yticklabels([])
#      axis[i,j].set_ylim(0,probmax)
#      axis[i,j].set_yscale('log')
#      axis[i,j].set_yticks([])
#      axis[i,j].set_xticklabels(xlabels)
#      axis[i,j].text(0.3, 0.23, txt)
      axis[i,j].set_title(Jugadores[i][j])
#      axis[i,j].plot([0.5,6.5],[prob, prob])
      axis[i,j].plot(a_range,prob_a[i][j])
  # once constructed all four histograms, save image
#  plt.savefig('aProbdist.png')
  plt.show()
  
  # return the relative probability of the models for each pplayer
  return mod1_mod0






savehistfigure(Dat,Jugadores)
#comparemodels01(Dat,Jugadores)



# auxiliar space to check formula
#Iter_l= ((l-3.5)*a_range[k]+p6)

#Iter_k=np.prod(    [ Iter_l for l in range(1,7)]**freq[i][j]   )

#prob_a[i,j]=[ Iter_k for k in range(atics)]

#[ np.prod(    [ ((l-3.5)*a_range[k]+p6) for l in range(1,7)]**freq[i][j]   ) for k in range(atics)]





