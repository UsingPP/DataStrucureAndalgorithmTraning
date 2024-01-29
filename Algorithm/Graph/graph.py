#그래프 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end = "")
    visited[s] = True

    for v in range(len(vtx)) :
        if adj[s][v] != 0 :
            if visited[v] == False :
                DFS(vtx, adj, v, visited)

vtx = ['U','V','W','X','Y']    
edge= [[0,  1,  1,  0,  0],    
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()

#너비 우선 탐색
from queue import Queue
def BFS_AL(vtx, aList, s) :
    n = len(vtx)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        print(vtx[s], end = " ")
        for v in aList[s] :
            if visited[v] is False :
                Q.put(v)
                visited[v] = True

vtx_bfs = ['U','V','W','X','Y']     # 정점 리스트
aList=[[1, 2],                  # 인접 리스트
       [0, 2, 3],   
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:W): ', end="")
BFS_AL(vtx_bfs, aList, 2)
print()

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx_bfs, aList, 0)
print()

#DFS를 이용한 신장 트리
def SpanningTree_DFS(vtx, adj, s, visited) :
    visited[s] = True
    for v in range(len(vtx)) :
        if adj[s][v] != 0 :
            if visited[v] == False :
                print( "(", vtx[s], vtx[v], ")", end = " ")
                SpanningTree_DFS(vtx, adj, v, visited)

print('SpanningTree_DFS(출발:U): ', end="")
SpanningTree_DFS(vtx, edge, 0, [False] * len(vtx))
print()

#BFS를 이용한 신장 트리
def SpanningTree_BFS(vtx, aList, s) :
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while Q.empty() == False :
        v = Q.get()
        for i in aList[v] :
            if visited[i] == False :
                Q.put(i)
                print("(", vtx[v], vtx[i] ,")", end = " ")
                visited[i] = True

print('SpanningTree_BFS(출발:U): ', end="")
SpanningTree_BFS(vtx_bfs, aList, 0)
print()