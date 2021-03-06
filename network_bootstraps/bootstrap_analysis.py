# -*- coding: utf-8 -*-
#Guillermo de Anda-Jáuregui
#Bootstrapped validation of networks
import networkx as nx
import os
import numpy as np
import pandas as pd
import math
#step 1 what is the network structure
#a) for each subtype, plot whole mutual information distribution
#b) identify min MI value for the 10000 interaction
#c) calculate equivalent p-value for number of samples and that MI
#step 2: repeat for bootstrapped neworks
#top k, top 100k, top million
#when single component is found, go through that interval until percolation
#maybe try the "cleaning less than 20 sized islands thing before 
#read a graph
panda_test = pd.read_table("test_case.sif",
                           header =None,)
panda_test = panda_test[[0,2,1]]
panda_list = panda_test.values.tolist()
def formatfunction(lista):
    return "{} {} {}".format(lista[0], lista[1], lista[2])
panda_reformat = []
for elem in panda_list:
    panda_reformat.append(formatfunction(elem))

panda_parse = nx.parse_edgelist(panda_reformat, 
                           nodetype = str, 
                           data=(('weight',float),)
                           )
G = panda_parse
#
G.edges(data = True)[9999]
#Functionalized 
def graphfromsif(sif):
    s = pd.read_table(sif,
                      header =None)
    s = s[[0,2,1]]
    s = s.values.tolist()
    def formatfunction(lista):
        return "{} {} {}".format(lista[0], lista[1], lista[2])
    reformat = []
    for elem in s:
        reformat.append(formatfunction(elem))
    g = nx.parse_edgelist(reformat, 
                           nodetype = str, 
                           data=(('weight',float),)
                           )
    return(g)
#MI p-value relationship
N = ""

def pvalue(mi, n):
    alfa = 1.062
    beta = -48.7
    gamma = -0.634
    #MI = (alfa - logP) / (-beta + (-gamma * n))
    p = math.exp(alfa -mi*(-beta + (-gamma * n)))
    return(p)
