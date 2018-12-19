#!/usr/bin/env python
# coding: utf-8

# In[52]:


from pygraph.classes.digraph import digraph
import math
import pandas as pd
import numpy as np
from collections import OrderedDict
import time
tStart = time.time()#計時開始

stop = 0.0001

def hits(G):
    hub = {}
    authority = {}
    
    allnodes = G.nodes()
    for node in allnodes:
        hub[node] = 1
        authority[node] = 1

    
    for i in range(100):
        change = 0.0
        
        #authority value
        norm = 0
        tmp = authority.copy()
        
        for node in allnodes:
            authority[node] = 0
            tmpnode= G.incidents(node)
            for incident_node in tmpnode:
                authority[node] += hub[incident_node]
            norm += pow(authority[node],2)
            
        norm = math.sqrt(norm)
        for node in allnodes:
            authority[node] = authority[node]/norm
            change += abs(tmp[node] - authority[node])
            
        #hub value
        norm = 0
        tmp = hub.copy()
        
        for node in allnodes:
            hub[node] = 0
            tmpnode = G.neighbors(node)
            for neighbor_node in tmpnode:
                hub[node] += authority[neighbor_node]
            norm += pow(hub[node],2)
        
        norm = math.sqrt(norm)
        for node in allnodes:
            hub[node] = hub[node]/norm
            change += abs(tmp[node] - hub[node])
            
        if change < stop:
            break
    
    tEnd = time.time()#計時結束
    print("The running time is: ", tEnd - tStart)

    #######列出全部#########
    print("\nThe authority are: ", authority)
    print("\nThe hub are: ", hub)
    
    #######排序後，列出全部#########
    #d_descending = OrderedDict(sorted(authority.items(), key=lambda kv: kv[1], reverse=True))
    #print(d_descending)
    #d_descending_hub = OrderedDict(sorted(hub.items(), key=lambda kv: kv[1], reverse=True))
    #print(d_descending_hub)
    



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
                
hits(graph)


# In[ ]:




