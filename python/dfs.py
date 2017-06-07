#!/usr/bin/python
import random

def dfs(src):
    if(visited[src] == True):
        return
    visited[src] = True
    print src,' -> ',
    for i in range(vertex):
        if((graph[src][i]) and (visited[i] ==False)):
            dfs(i)              
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
    for i in range(vertex):
        dfs(i)
    print ' end'
    return

if __name__ == '__main__':
    main()
