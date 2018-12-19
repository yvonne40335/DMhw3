#!/usr/bin/env python
# coding: utf-8

# In[41]:


from pygraph.classes.digraph import digraph
import math
import pandas as pd
import numpy as np
import time
tStart = time.time()#計時開始

stop = 0.0001

def simrank(G):
    c = 0.85
    allnodes = G.nodes()
    count = len(allnodes)
    sim = np.identity(count)
    
    for i in range(30):
        change = 0.0
        tmp = sim.copy()
        a = 0
        b = 0
        for nodeA in allnodes:
            for nodeB in allnodes:
                tmpnodeA= G.incidents(nodeA)
                tmpnodeB= G.incidents(nodeB)
                if nodeA == nodeB:
                    sim[a][b] = 1
                elif len(tmpnodeA)==0 or len(tmpnodeB)==0:
                    sim[a][b] = 0
                else:
                    tmpsim = 0
                    for Ia in tmpnodeA:
                        for Ib in tmpnodeB:
                            tmpsim += sim[order[Ia]][order[Ib]]
                    sim[a][b] = c/(len(tmpnodeA)*len(tmpnodeB)) * tmpsim
                    change += abs(sim[a][b] - tmp[a][b])
                b = b + 1
            a = a + 1
            b = 0
            
        if change < stop:
            break

    tEnd = time.time()#計時結束
    print("The running time is: ", tEnd - tStart)
    
    #######列出全部#########
    print("\nThe simrank are:\n", sim)
    
    #######列出平均值#########
    #print("\nThe mean of simrank is:\n", sim.mean())
                

alldata = []
order = {}
index = 0
graph = digraph()
contents = open("graph_1.txt",'r').read().split('\n')
for line in contents:
    line = line.split(',')

    if line[0] not in alldata:
        graph.add_nodes([line[0]])
        alldata.append(line[0])
        order[line[0]]=index
        index = index + 1
    if line[1] not in alldata:
        graph.add_nodes([line[1]])
        alldata.append(line[1])
        order[line[1]]=index
        index = index + 1
    graph.add_edge((line[0], line[1]))

#######列出順序#########
#print("order of nodes:",order.keys())
simrank(graph)


# In[ ]:




