from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    print("BFS:", end=" ")
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors that are not visited
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    print()

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS
bfs(graph, 'A')
