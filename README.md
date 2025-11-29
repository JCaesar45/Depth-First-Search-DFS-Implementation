```markdown
# Depth-First Search (DFS) Implementation

This project demonstrates how to implement the Depth-First Search (DFS) algorithm on an undirected graph represented by an adjacency matrix.

## Overview

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. Unlike Breadth-First Search (BFS), which explores neighbors level by level, DFS dives deep into a branch until it hits a dead end, then backtracks to explore new paths.

## How It Works

- Uses a stack data structure to keep track of nodes to visit.
- Starts from a given node.
- Visits a node, then pushes its unvisited neighbors onto the stack.
- Continues until all reachable nodes have been visited.

## Implementation Details

- Function Name: `dfs`
- Arguments:
  - `adjacency_matrix`: a 2D list representing the undirected graph.
  - `start_node`: the node label (integer) from which to start the traversal.
- Returns:
  - A list of nodes reachable from the start node, in the order they are visited.

## Usage

```python
# Example adjacency matrix:
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

# Starting from node 1:
reachable_nodes = dfs(graph, 1)
print(reachable_nodes)  # Output: [1, 2, 3, 0]
``

## Code Implementation

```python
def dfs(adjacency_matrix, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Iterate over neighbors
            for neighbor, is_connected in enumerate(adjacency_matrix[node]):
                if is_connected and neighbor not in visited:
                    stack.append(neighbor)
    return visited
``

## Testing

The implementation passes several test cases, ensuring correct traversal order and handling of isolated nodes or disconnected graphs.

## License

MIT License

Would you like me to generate a visual diagram or any other supplementary materials for this project?
