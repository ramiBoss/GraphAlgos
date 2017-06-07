import sys
def dfs(v, vertex, visited, graph):
    visited[v] = 1
    print v,"-> ",
    for i in range(vertex):
        if(visited[i] == 0 and graph[v][i] == 1):
            dfs(i, vertex, visited, graph)
        elif((visited[i] == 1 or visited[i] == 2) and graph[v][i] == 1):
            print "Cycle Found Between ", v, " ->", i
            sys.exit()
    visited[v] = 2
    return

def dft(vertex, graph):
    visited = []
    for i in range(vertex):
        visited.append(0)
    for i in range(vertex):
        if visited[i] == 0:
            print "\nNew Tree: "
            dfs(i, vertex, visited, graph)
    return
    
def main():
    vertex = 4
    graph = [[0,0 ,0,0],
             [0,0,1,0],
             [0,1,0,0],
             [0,0,0,0]]
    dft(vertex, graph)
    return
if __name__ == "__main__":
    main()
