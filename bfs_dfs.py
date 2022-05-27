graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited_lis = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited_lis, graph, node): #function for BFS
    visited_lis.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited_lis:
                visited_lis.append(neighbour)
                queue.append(neighbour)

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Enter Your Choice: \n1. For BFS \n2. For DFS \nChoice = ", end="")
ch = int(input())

if(ch == 1):
    # Driver Code
    print("Following is the Breadth-First Search")
    bfs(visited_lis, graph, '5')    # function calling
elif(ch == 2):
    # Driver Code
    print("Following is the Depth-First Search")
    dfs(visited, graph, '5')
else:
    print("Thanks for visiting....")