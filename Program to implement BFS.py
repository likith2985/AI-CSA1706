"""
This program implements the Breadth-First Search (BFS) algorithm.
BFS is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'),
and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
"""

from collections import deque

def bfs(graph, start_node):
    """
    Performs Breadth-First Search on a graph.

    Args:
        graph (dict): A dictionary representing the graph as an adjacency list.
                      Keys are nodes, and values are lists of their neighbors.
        start_node: The node from which to start the BFS traversal.

    Returns:
        list: A list of nodes in the order they were visited.
              Returns an empty list if the start_node is not in the graph.
    """
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in the graph.")
        return []

    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Initialize a queue with the start node
    bfs_order = []  # To store the order of visited nodes

    visited.add(start_node)

    while queue:
        current_node = queue.popleft()  # Dequeue a vertex from queue
        bfs_order.append(current_node)

        # Get all adjacent vertices of the dequeued vertex current_node.
        # If an adjacent has not been visited, then mark it visited and enqueue it.
        for neighbor in graph.get(current_node, []): # Use .get for safety if a node has no outgoing edges listed
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return bfs_order

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    # This graph is undirected for simplicity in this example.
    # For a directed graph, the adjacency list would represent outgoing edges.
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
    print(f"Starting BFS from node: {start_node_example}")
    bfs_result = bfs(example_graph, start_node_example)
    if bfs_result:
        print(f"BFS traversal order: {bfs_result}")
    print("-"*30)

    start_node_example_2 = 'D'
    print(f"Starting BFS from node: {start_node_example_2}")
    bfs_result_2 = bfs(example_graph, start_node_example_2)
    if bfs_result_2:
        print(f"BFS traversal order: {bfs_result_2}")
    print("-"*30)

    # Example of a disconnected component or a node not in the main graph structure
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
    print(f"Starting BFS from node: {start_node_isolated} (component 1)")
    bfs_result_isolated = bfs(example_graph_with_isolated, start_node_isolated)
    if bfs_result_isolated:
        print(f"BFS traversal order: {bfs_result_isolated}")
    print("-"*30)

    start_node_isolated_2 = 'X'
    print(f"Starting BFS from node: {start_node_isolated_2} (component 2)")
    bfs_result_isolated_2 = bfs(example_graph_with_isolated, start_node_isolated_2)
    if bfs_result_isolated_2:
        print(f"BFS traversal order: {bfs_result_isolated_2}")
    print("-"*30)

    start_node_not_in_graph = 'Z'
    print(f"Starting BFS from node: {start_node_not_in_graph} (not in graph)")
    bfs_result_not_in_graph = bfs(example_graph, start_node_not_in_graph)
    # The function itself will print an error message
    if bfs_result_not_in_graph:
        print(f"BFS traversal order: {bfs_result_not_in_graph}")
    else:
        print("BFS traversal not possible as start node is not in the graph.")

