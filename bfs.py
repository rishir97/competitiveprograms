# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque

l=[]

def bfs(graph,start):
    visited=[False for i in range(len(graph))]
    q=deque()
    q.append(start)
    visited[start]=True
    while len(q):
        v=q.popleft()
        l.append(v)
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i]=True

graph={}
#graph[0]=[1,2]
#graph[1]=[2]
#graph[2]=[0,3]
#graph[3]=[3]
vertex=int(input('enter number of vertices : '))
for i in range(vertex):
    print('enter the connected vertices to vertex ',i)
    graph[i]=list(map(int,input().split(' ')))

bfs(graph,2)

print('path:', *l, sep='->')