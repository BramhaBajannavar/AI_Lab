def dfs(graph, start, goal, depth, visited, path_traversed):
    path_traversed.append(start)

    if depth == 0:
        if start == goal:
            return [start]
        return None

    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, depth - 1, visited, path_traversed)
            if path:
                return [start] + path
    return None

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        visited = set()
        path_traversed = [] 
        print(f"\n--- Depth {depth} ---")
        path = dfs(graph, start, goal, depth, visited, path_traversed)
        
        print("Nodes traversed:", " -> ".join(path_traversed))
        
        if path:
            return path
    return None

graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': ['h'],
    'e': ['i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []
}

start = 'a'
goal = 'g'
max_depth = 5

result = iddfs(graph, start, goal, max_depth)
print("\nFinal Path:", result)
