#!/usr/bin/python
import Queue
import random

def bfs(src):
    if visited[src] == True:
        return
    visited[src] = True
    q = Queue.Queue()
    q.put(src)
    while not q.empty():
        u = q.get()
        print u,' ->',
        for i in range(vertex):
            if(graph[u][i] and (visited[i] == False)):
                q.put(i)
                visited[i] = True
                
    
    return

def main():
    global graph
    global vertex
    global visited
    print '1: Enter manually\n 2: Randomize\n'
    choice = raw_input()

    if(int(choice) == 1):
        vertex = raw_input('Number of vertex: ')
        graph = [[0 for x in range(vertex)] for y in range(vertex)]
        print 'Enter the graph matrix: '
        for i in range(vertex):
            for j in range(vertex):
                graph[i][j] = raw_input()
    elif(int(choice) == 2):
        vertex = random.randint(2,4)
        graph = [[0 for x in range(vertex)] for y in range(vertex)]
        vis = [[False for x in range(vertex)] for y in range(vertex)]
        for i in range(vertex):
            for j in range(vertex):
                if(i == j):
                    graph[i][j] = 0
                elif(vis[j][i]):
                    graph[i][j] = graph[j][i]                          
                else:
                    graph[i][j] = random.randint(0,1)
                    vis[i][j] = True
    else:
        print 'Wrong Input...............'
        print 'Terminating...............'

    visited = [False]*vertex
    print 'Graph Info: '
    print 'Number of Vertices: ', vertex
    print 'Graph'
    print graph
    k = 0
    for i in range(vertex):
        print 'Tree : ', k,' ::',
        k = k+1
        bfs(i)
        print ' end\n'
    return

if __name__ == '__main__':
    main()

