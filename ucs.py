
#from collections import deque
from queue import PriorityQueue

l={}
k=[]
def ucs(graph,start,end):
    
    q=PriorityQueue()
    q.put((0,"0"))
    while not q.empty():
        v=q.get()
        c=int(v[1][-1])
        if c==end:
           print("goal reach cost:",v[0])
           print(*v[1],sep='->')
           return
        else:
            for i in graph[c]:
                q.put((i[0]+v[0],v[1]+str(i[1])))
            
      
        
graph={}
graph[0]=[[1,1],[12,5]]
graph[1]=[[3,2],[1,3]]
graph[2]=[[3,4]]
graph[3]=[[1,4],[2,5]]
graph[4]=[[3,5]]
graph[5]=[]
#vertex=int(input('enter number of vertices : '))
#for i in range(vertex):
#    print('enter the connected vertices to vertex ',i)
#    graph[i]=list(map(int,input().split(' ')))

ucs(graph,0,5)

#print('path:', *k, sep='->')
#print(l)