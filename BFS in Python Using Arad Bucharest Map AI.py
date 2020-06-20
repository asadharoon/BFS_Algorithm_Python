# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:42:15 2020

@author: AsadHaroon
"""


graph={
       "Arad":{"Sibiu":140,"Timisoara":118,"Zerind":75},
       "Timisoara":{"Lugoj":111,"Arad":118},
       "Lugoj":{"Mehadia":70,"Timisoara":111},
       "Mehadia":{"Dobreta":75,"Lugoj":70},
       "Dobreta":{"Craiova":120,"Mehadia":75},
       "Craiova":{"Rimnicu Vilcea":146,"Pitesti":138,"Dobreta":120},
       "Rimnicu Vilcea":{"Sibiu":80,"Pitesti":97,"Craiova":146},
       "Sibiu":{"Arad":140,"Fagaras":99,"Rimnicu Vilcea":80},
       "Zerind":{"Oradea":71,"Arad":75},
       "Oradea":{"Sibiu":151,"Zerind":71},
       "Fagaras":{"Bucharest":211,"Sibiu":99},
       "Pitesti":{"Rimnicu Vilcea":97,"Craiova":138,"Bucharest":101},
       "Bucharest":{"Giurgui":90,"Fagaras":211,"Pitesti":101,"Urziceni":85},
       "Urziceni":{"Bucharest":85,"Hirsova":98,"Vaslui":142},
       "Hirsova":{"Urziceni":98,"Eforie":86},
       "Eforie":{"Hirsova":86},
       "Vaslui":{"Urziceni":142,"lasi":92},
       "lasi":{"Vaslui":92,"Neamt":87},
       "Neamt":{"lasi":87},
       "Giurgui":{"Bucharest":90}
       
       }
def bfs(graph,start):
    if not start in graph.keys():
        return None
    visited=[]
    path=[]
    q=[]
    visited.append(start)
    path.append(start)
    for node in graph[start]:
        q.append(node)
    while len(q)!=0:
        node=q.pop(0)
        if node not in visited: 
            path.append(node)
        for n in graph[node]:
            if n not in visited:
                q.append(n)
        visited.append(node)
    return path

a=bfs(graph,'Arad')
print("\nBFS Traversal is "+str(a))