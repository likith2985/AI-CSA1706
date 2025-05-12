"""
This program implements the Depth-First Search (DFS) algorithm.
DFS is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
and explores as far as possible along each branch before backtracking.
"""

def dfs_recursive(graph, node, visited, dfs_order):
    """Recursive helper function for DFS."""
    visited.add(node)
    dfs_order.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, dfs_order)

def dfs(graph, start_node):
    """
    Performs Depth-First Search on a graph using a recursive approach.

    Args:
        graph (dict): A dictionary representing the graph as an adjacency list.
                      Keys are nodes, and values are lists of their neighbors.
        start_node: The node from which to start the DFS traversal.

    Returns:
        list: A list of nodes in the order they were visited (one possible DFS order).
              Returns an empty list if the start_node is not in the graph.
    """
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []

    visited = set()  # To keep track of visited nodes
    dfs_order = []   # To store the order of visited nodes
    
    dfs_recursive(graph, start_node, visited, dfs_order)
    
    return dfs_order

def dfs_iterative(graph, start_node):
    """
    Performs Depth-First Search on a graph using an iterative approach (with a stack).

    Args:
        graph (dict): A dictionary representing the graph as an adjacency list.
        start_node: The node from which to start the DFS traversal.

    Returns:
        list: A list of nodes in the order they were visited (one possible DFS order).
              Returns an empty list if the start_node is not in the graph.
    """
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []

    visited = set()
    stack = [start_node] # Use a list as a stack
    dfs_order = []

    while stack:
        node = stack.pop() # Pop the last element (LIFO)

        if node not in visited:
            visited.add(node)
            dfs_order.append(node)

            # Add neighbors to the stack in reverse order to visit them in standard order
            # (e.g., if neighbors are [B, C], add C then B, so B is processed first)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return dfs_order


if __name__ == "__main__":
    example_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    print("Graph (Adjacency List):")
    for node, neighbors in example_graph.items():
        print(f"  {node}: {neighbors}")
    print("-"*30)

    start_node_example = 'A'
    print(f"Starting DFS (Recursive) from node: {start_node_example}")
    dfs_result_recursive = dfs(example_graph, start_node_example)
    if dfs_result_recursive:
        print(f"DFS traversal order (Recursive): {dfs_result_recursive}")
    print("-"*30)

    print(f"Starting DFS (Iterative) from node: {start_node_example}")
    dfs_result_iterative = dfs_iterative(example_graph, start_node_example)
    if dfs_result_iterative:
        print(f"DFS traversal order (Iterative): {dfs_result_iterative}")
    print("-"*30)

    start_node_example_2 = 'D'
    print(f"Starting DFS (Recursive) from node: {start_node_example_2}")
    dfs_result_recursive_2 = dfs(example_graph, start_node_example_2)
    if dfs_result_recursive_2:
        print(f"DFS traversal order (Recursive): {dfs_result_recursive_2}")
    print("-"*30)
    
    print(f"Starting DFS (Iterative) from node: {start_node_example_2}")
    dfs_result_iterative_2 = dfs_iterative(example_graph, start_node_example_2)
    if dfs_result_iterative_2:
        print(f"DFS traversal order (Iterative): {dfs_result_iterative_2}")
    print("-"*30)

    example_graph_with_isolated = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B'],
        'X': ['Y'],
        'Y': ['X']
    }
    print("Graph with disconnected component:")
    for node, neighbors in example_graph_with_isolated.items():
        print(f"  {node}: {neighbors}")
    print("-"*30)
    
    start_node_isolated = 'A'
    print(f"Starting DFS (Recursive) from node: {start_node_isolated} (component 1)")
    dfs_result_isolated_rec = dfs(example_graph_with_isolated, start_node_isolated)
    if dfs_result_isolated_rec:
        print(f"DFS traversal order (Recursive): {dfs_result_isolated_rec}")
    print("-"*30)

    print(f"Starting DFS (Iterative) from node: {start_node_isolated} (component 1)")
    dfs_result_isolated_iter = dfs_iterative(example_graph_with_isolated, start_node_isolated)
    if dfs_result_isolated_iter:
        print(f"DFS traversal order (Iterative): {dfs_result_isolated_iter}")
    print("-"*30)

    start_node_not_in_graph = 'Z'
    print(f"Starting DFS (Recursive) from node: {start_node_not_in_graph} (not in graph)")
    dfs_result_not_in_graph_rec = dfs(example_graph, start_node_not_in_graph)
    if not dfs_result_not_in_graph_rec:
        print("DFS traversal not possible as start node is not in the graph (Recursive).")
    print("-"*30)

    print(f"Starting DFS (Iterative) from node: {start_node_not_in_graph} (not in graph)")
    dfs_result_not_in_graph_iter = dfs_iterative(example_graph, start_node_not_in_graph)
    if not dfs_result_not_in_graph_iter:
        print("DFS traversal not possible as start node is not in the graph (Iterative).")

