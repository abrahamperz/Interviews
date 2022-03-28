graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[]
}
visited = set()
def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neihbour in graph[root]:
            dfs(visited, graph, neihbour)

dfs(visited,graph, 'A')
