from collections import deque

def water_jug_solver(jug1_capacity, jug2_capacity, target_amount):
    """Solves the Water Jug problem using BFS."""
    q = deque()
    visited = set()
    initial_state = (0, 0)
    q.append((initial_state, []))
    visited.add(initial_state)

    while q:
        (current_jug1, current_jug2), path = q.popleft()
        if current_jug1 == target_amount or current_jug2 == target_amount:
            path.append((current_jug1, current_jug2))
            return path
        next_states = []
        next_states.append(((jug1_capacity, current_jug2), "Fill Jug1"))
        next_states.append(((current_jug1, jug2_capacity), "Fill Jug2"))
        next_states.append(((0, current_jug2), "Empty Jug1"))
        next_states.append(((current_jug1, 0), "Empty Jug2"))
        pour_amount = min(current_jug1, jug2_capacity - current_jug2)
        next_states.append(((current_jug1 - pour_amount, current_jug2 + pour_amount), "Pour Jug1 to Jug2"))
        pour_amount = min(current_jug2, jug1_capacity - current_jug1)
        next_states.append(((current_jug1 + pour_amount, current_jug2 - pour_amount), "Pour Jug2 to Jug1"))

        for (state, action_description) in next_states:
            if state not in visited:
                new_path = path + [(current_jug1, current_jug2), action_description]
                q.append((state, new_path))
                visited.add(state)

    return None 

if __name__ == "__main__":
    jug1_cap = 4
    jug2_cap = 3
    target = 2

    print(f"Attempting to solve Water Jug Problem for Jug1={jug1_cap}L, Jug2={jug2_cap}L, Target={target}L\n")
    solution_path = water_jug_solver(jug1_cap, jug2_cap, target)

    if solution_path:
        print("Solution found!")
        print("Initial state: (0, 0)")
        current_state = (0,0)
        for i in range(0, len(solution_path) -1 , 2):
            action = solution_path[i+1]
            next_state = solution_path[i+2] if i+2 < len(solution_path) else solution_path[-1]
            if isinstance(next_state, str): 
                next_state = solution_path[-1]

            print(f"Step: {action} -> State: {next_state}")
            current_state = next_state
        if current_state[0] != target and current_state[1] != target:
          
             pass 

    else:
        print("No solution found.")

    jug1_cap_2 = 2
    jug2_cap_2 = 6
    target_2 = 5
    print(f"\nAttempting to solve Water Jug Problem for Jug1={jug1_cap_2}L, Jug2={jug2_cap_2}L, Target={target_2}L\n")
    solution_path_2 = water_jug_solver(jug1_cap_2, jug2_cap_2, target_2)
    if solution_path_2:
        print("Solution found!")
        current_state = (0,0)
        print("Initial state: (0, 0)")
        for i in range(0, len(solution_path_2) -1 , 2):
            action = solution_path_2[i+1]
            next_state = solution_path_2[i+2] if i+2 < len(solution_path_2) else solution_path_2[-1]
            print(f"Step: {action} -> State: {next_state}")
    else:
        print("No solution found. (Target is odd, capacities are even)")

    jug1_cap_3 = 5
    jug2_cap_3 = 3
    target_3 = 4
    print(f"\nAttempting to solve Water Jug Problem for Jug1={jug1_cap_3}L, Jug2={jug2_cap_3}L, Target={target_3}L\n")
    solution_path_3 = water_jug_solver(jug1_cap_3, jug2_cap_3, target_3)
    if solution_path_3:
        print("Solution found!")
        current_state = (0,0)
        print("Initial state: (0, 0)")
        for i in range(0, len(solution_path_3) -1 , 2):
            action = solution_path_3[i+1]
            next_state = solution_path_3[i+2] if i+2 < len(solution_path_3) else solution_path_3[-1]
            print(f"Step: {action} -> State: {next_state}")
    else:
        print("No solution found.")


