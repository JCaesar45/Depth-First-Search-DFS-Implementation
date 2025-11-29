def dfs(adjacency_matrix, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor, is_connected in enumerate(adjacency_matrix[node]):
                if is_connected and neighbor not in visited:
                    stack.append(neighbor)

    return visited
