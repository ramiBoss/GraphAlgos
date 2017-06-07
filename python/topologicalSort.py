stack = []
def topoSort(v, vertex, graph, visited):
    visited[v] = 1
    for i in range(vertex):
        if(visited[i] == 0 and graph[v][i]):
            topoSort(i, vertex, graph, visited)
    stack.append(v)
    return

def tps(vertex, graph):
    visited = []
    for i in range(vertex):
        visited.append(0)
    for i in range(vertex):
        if(visited[i] == 0):
            topoSort(i, vertex, graph, visited)

    for i in range(vertex):
        print stack.pop();
    return 

    

def main():
    vertex = 9
    graph = [[0,1,0,0,0,0,0,1,0],
             [0,0,1,0,0,0,0,1,0],
             [0,0,0,0,0,1,0,0,0],
             [0,0,1,0,1,0,0,0,0],
             [0,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]
    tps(vertex, graph)
    return



if __name__ == "__main__":
    main()
