#!/usr/bin/env python
# coding: utf-8

# In[25]:


from pygraph.classes.digraph import digraph
import math
import pandas as pd
import numpy as np
from collections import OrderedDict
import time
tStart = time.time()#計時開始


stop = 0.0001

def pagerank(G):
    
    pr = {}
    d = 0.15
    allnodes = G.nodes()
    count = len(allnodes)
    
    for node in allnodes:
            if len(G.neighbors(node)) == 0:
                for other in G.nodes():
                    digraph.add_edge(G, (node, other))
    
    for node in allnodes:
        pr[node] = 1/count

    for i in range(100):
        change = 0.0
        tmp = pr.copy()
        for node in allnodes:
            pr[node] = 0
            tmpnode= G.incidents(node)
            for incident_node in tmpnode:
                pr[node] += tmp[incident_node]/len(G.neighbors(incident_node))
            pr[node] = (1-d)*pr[node]+ d/count
            change += abs(tmp[node] - pr[node])
            
        if change < stop:
            break
     
    tEnd = time.time()#計時結束
    print("The running time is: ", tEnd - tStart)
    
    #######列出全部#########
    print("\nThe pagerank are: ", pr)
    
    #######排序後，列出全部#########
    #d_descending = OrderedDict(sorted(pr.items(), key=lambda kv: kv[1], reverse=True))
    #print(d_descending)

                

alldata = []
graph = digraph()
file_name = "graph_1.txt" #################################### please change file name here #################################
contents = open(file_name,'r').read().split('\n')

if file_name=="graph_7.txt":
    for line in contents:
        line = line.split()
        del line[0:1]
    
        line[0]="C"+line[0]
    
        if line[0] not in alldata:
            graph.add_nodes([line[0]])
            alldata.append(line[0])
        if line[1] not in alldata:
            graph.add_nodes([line[1]])
            alldata.append(line[1])
        graph.add_edge((line[0], line[1]))
else:
    for line in contents:
        line = line.split(',')

        if line[0] not in alldata:
            graph.add_nodes([line[0]])
            alldata.append(line[0])
        if line[1] not in alldata:
            graph.add_nodes([line[1]])
            alldata.append(line[1])
        graph.add_edge((line[0], line[1]))


pagerank(graph)


# In[ ]:




