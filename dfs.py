# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 02:49:29 2018

@author: Administrator
"""

l=[]
def dfs(graph,start):
    visited=[False for i in range(len(graph))]
    q=[]
    q.append(start)
    visited[start]=True
    while len(q):
        v=q.pop()
        l.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
        


graph={}
#graph[0]=[1,2]
#graph[1]=[2]
#graph[2]=[0,3]
#graph[3]=[3]
vertex=int(input('enter number of vertices : '))
for i in range(vertex):
    print('enter the connected vertices to vertex ',i)
    graph[i]=list(map(int,input().split(' ')))

dfs(graph,int(input('Enter the starting vertex: ')))

print('path:', *l, sep='->')