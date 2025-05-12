"""
This program implements a solution to the Travelling Salesman Problem (TSP)
using a brute-force approach. This approach finds the shortest possible route
that visits each city exactly once and returns to the origin city.

Note: The brute-force approach has a time complexity of O(n!), where n is
the number of cities. This makes it impractical for a large number of cities.
For more than a small number of cities (e.g., >10-12), more advanced algorithms
like dynamic programming (Held-Karp), branch and bound, or heuristics
(e.g., nearest neighbor, genetic algorithms, simulated annealing) are required.
"""

import itertools
import math

def calculate_distance(point1, point2):
    """Calculates the Euclidean distance between two points (cities)."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def solve_tsp_brute_force(cities, distance_matrix=None):
    """
    Solves the TSP using a brute-force approach by checking all permutations.

    Args:
        cities (list of tuples): A list where each tuple represents the (x, y) coordinates of a city.
                                 Alternatively, if distance_matrix is provided, this can be a list of city indices [0, 1, ..., n-1].
        distance_matrix (list of lists, optional): A precomputed matrix where distance_matrix[i][j]
                                                   is the distance between city i and city j.
                                                   If None, distances are calculated using Euclidean distance from `cities` coordinates.

    Returns:
        tuple: (min_distance, best_path)
               min_distance (float): The shortest distance found.
               best_path (list): The sequence of cities in the shortest path, including the return to the start.
               Returns (float("inf"), []) if there are fewer than 2 cities.
    """
    num_cities = len(cities)
    if num_cities < 2:
        if num_cities == 1 and distance_matrix is None:
             return 0, [cities[0], cities[0]] # Path from city to itself
        elif num_cities == 1 and distance_matrix is not None:
             return 0, [0,0]
        return float("inf"), []

    # If distance_matrix is not provided, create one from city coordinates
    if distance_matrix is None:
        adj_matrix = [[0] * num_cities for _ in range(num_cities)]
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    adj_matrix[i][j] = calculate_distance(cities[i], cities[j])
        city_indices = list(range(num_cities))
    else:
        adj_matrix = distance_matrix
        city_indices = list(range(num_cities)) # Assume cities are indexed 0 to n-1

    # Start from the first city (index 0)
    start_city_index = city_indices[0]
    other_city_indices = city_indices[1:]

    min_distance = float("inf")
    best_path_indices = []

    # Generate all permutations of other cities
    for perm in itertools.permutations(other_city_indices):
        current_path_distance = 0
        current_path_indices = [start_city_index] + list(perm)

        # Calculate distance for the current path
        # From start_city to the first city in permutation
        current_distance = adj_matrix[start_city_index][perm[0]]
        current_path_distance += current_distance

        # Distances between cities in the permutation
        for i in range(len(perm) - 1):
            current_distance = adj_matrix[perm[i]][perm[i+1]]
            current_path_distance += current_distance

        # Distance from the last city in permutation back to the start_city
        current_distance = adj_matrix[perm[-1]][start_city_index]
        current_path_distance += current_distance

        if current_path_distance < min_distance:
            min_distance = current_path_distance
            best_path_indices = current_path_indices + [start_city_index] # Add return to start

    # If using coordinates, map indices back to city coordinates for the path
    if distance_matrix is None:
        best_path_coords = [cities[i] for i in best_path_indices]
        return min_distance, best_path_coords
    else:
        return min_distance, best_path_indices

if __name__ == "__main__":
    # Example 1: Using city coordinates
    print("Example 1: Using City Coordinates")
    city_coordinates = [
        (0, 0),  # City 0 (A)
        (1, 5),  # City 1 (B)
        (2, 2),  # City 2 (C)
        (5, 1)   # City 3 (D)
    ]
    print(f"City Coordinates: {city_coordinates}")
    min_dist_coords, best_p_coords = solve_tsp_brute_force(city_coordinates)
    if best_p_coords:
        print(f"Shortest distance: {min_dist_coords:.2f}")
        print(f"Best path (coordinates): {best_p_coords}")
    else:
        print("Could not find a solution.")
    print("-"*40)

    # Example 2: Using a precomputed distance matrix
    print("Example 2: Using a Precomputed Distance Matrix")
    # For cities A, B, C, D (0, 1, 2, 3)
    # A->B, A->C, A->D
    # B->A, B->C, B->D
    # etc.
    dist_matrix = [
        [0, 10, 15, 20], # Distances from City 0 (A)
        [10, 0, 35, 25], # Distances from City 1 (B)
        [15, 35, 0, 30], # Distances from City 2 (C)
        [20, 25, 30, 0]  # Distances from City 3 (D)
    ]
    cities_for_matrix = list(range(len(dist_matrix))) # [0, 1, 2, 3]
    print(f"Number of cities: {len(cities_for_matrix)}")
    print("Distance Matrix:")
    for row in dist_matrix:
        print(row)
    
    min_dist_matrix, best_p_matrix = solve_tsp_brute_force(cities_for_matrix, distance_matrix=dist_matrix)
    if best_p_matrix:
        print(f"Shortest distance: {min_dist_matrix}") # Exact since matrix is int
        # Path will be indices, e.g., [0, 1, 3, 2, 0] means A -> B -> D -> C -> A
        city_names = ["A", "B", "C", "D"]
        named_path = [city_names[i] for i in best_p_matrix]
        print(f"Best path (indices): {best_p_matrix}")
        print(f"Best path (named): {' -> '.join(named_path)}")

    else:
        print("Could not find a solution.")
    print("-"*40)

    # Example 3: Fewer than 2 cities
    print("Example 3: Fewer than 2 cities")
    city_coords_single = [(0,0)]
    min_dist_single, best_p_single = solve_tsp_brute_force(city_coords_single)
    print(f"Single city: Distance: {min_dist_single}, Path: {best_p_single}")

    city_coords_none = []
    min_dist_none, best_p_none = solve_tsp_brute_force(city_coords_none)
    print(f"No cities: Distance: {min_dist_none}, Path: {best_p_none}")
    print("-"*40)

    # Example 4: A slightly larger set of cities (will be slow)
    # For 5 cities, (5-1)! = 4! = 24 permutations. Manageable.
    # For 6 cities, (6-1)! = 5! = 120 permutations. Still okay.
    # For 10 cities, (10-1)! = 9! = 362,880 permutations. Getting slow.
    # For 11 cities, (11-1)! = 10! = 3,628,800 permutations. Very slow.
    print("Example 4: 5 Cities (Coordinates)")
    city_coordinates_5 = [
        (0,0), (1,10), (5,2), (8,8), (3,6)
    ]
    print(f"City Coordinates: {city_coordinates_5}")
    min_dist_5, best_p_5 = solve_tsp_brute_force(city_coordinates_5)
    if best_p_5:
        print(f"Shortest distance: {min_dist_5:.2f}")
        print(f"Best path (coordinates): {best_p_5}")
    else:
        print("Could not find a solution.")


