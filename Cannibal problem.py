"""
This program solves the Missionaries and Cannibals problem using Breadth-First Search (BFS).

The problem: Three missionaries and three cannibals are on one side of a river,
along with a boat that can hold one or two people. Find a way to get everyone
to the other side, without ever leaving a group of missionaries in one place
outnumbered by the cannibals in that place.
"""

from collections import deque

# N represents the number of missionaries and cannibals (default is 3)
N_PERSONS = 3
BOAT_CAPACITY = 2

class State:
    def __init__(self, missionaries_left, cannibals_left, boat_on_left_bank):
        self.ml = missionaries_left  # Missionaries on the left bank
        self.cl = cannibals_left    # Cannibals on the left bank
        self.bl = boat_on_left_bank # 1 if boat is on left bank, 0 if on right bank

        # Missionaries and cannibals on the right bank are derived
        self.mr = N_PERSONS - self.ml
        self.cr = N_PERSONS - self.cl

    def is_valid(self):
        # Check if missionaries are outnumbered on the left bank
        if self.ml > 0 and self.ml < self.cl:
            return False
        # Check if missionaries are outnumbered on the right bank
        if self.mr > 0 and self.mr < self.cr:
            return False
        # Check for valid numbers (0 to N_PERSONS)
        if not (0 <= self.ml <= N_PERSONS and 0 <= self.cl <= N_PERSONS):
            return False
        return True

    def is_goal(self):
        return self.ml == 0 and self.cl == 0 and self.bl == 0

    def __eq__(self, other):
        return self.ml == other.ml and self.cl == other.cl and self.bl == other.bl

    def __hash__(self):
        return hash((self.ml, self.cl, self.bl))

    def __str__(self):
        return f"(M_L={self.ml}, C_L={self.cl}, Boat_L={self.bl} | M_R={self.mr}, C_R={self.cr})"

def get_possible_next_states(current_state):
    """Generates all valid successor states from the current state."""
    next_states = []
    possible_moves = [] # (missionaries_in_boat, cannibals_in_boat)
    for m_boat in range(BOAT_CAPACITY + 1):
        for c_boat in range(BOAT_CAPACITY + 1):
            if 1 <= m_boat + c_boat <= BOAT_CAPACITY:
                possible_moves.append((m_boat, c_boat))

    for m_moved, c_moved in possible_moves:
        if current_state.bl == 1: # Boat is on the left bank, moving to right
            if current_state.ml >= m_moved and current_state.cl >= c_moved:
                new_state = State(current_state.ml - m_moved, 
                                  current_state.cl - c_moved, 
                                  0)
                action_description = f"Move {m_moved}M, {c_moved}C from Left to Right"
                if new_state.is_valid():
                    next_states.append((new_state, action_description))
        else: # Boat is on the right bank, moving to left
            if current_state.mr >= m_moved and current_state.cr >= c_moved:
                new_state = State(current_state.ml + m_moved, 
                                  current_state.cl + c_moved, 
                                  1)
                action_description = f"Move {m_moved}M, {c_moved}C from Right to Left"
                if new_state.is_valid():
                    next_states.append((new_state, action_description))
    return next_states

def solve_missionaries_cannibals():
    """Solves the Missionaries and Cannibals problem using BFS."""
    initial_state = State(N_PERSONS, N_PERSONS, 1)
    if not initial_state.is_valid():
        return "Initial state is invalid!"

    queue = deque([(initial_state, [])]) # Each item is (state, path_to_state_with_actions)
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state.is_goal():
            return path + [("Goal Reached", current_state)]

        for next_s, action in get_possible_next_states(current_state):
            if next_s not in visited:
                visited.add(next_s)
                new_path = path + [(action, current_state)] # Store action and state before action
                queue.append((next_s, new_path))
    
    return "No solution found."

if __name__ == "__main__":
    print(f"Solving Missionaries and Cannibals Problem for {N_PERSONS} pairs with boat capacity {BOAT_CAPACITY}:\n")
    solution = solve_missionaries_cannibals()

    if isinstance(solution, str): # Error message or no solution
        print(solution)
    else:
        print("Solution found!")
        print("Initial State: (M_L=3, C_L=3, Boat_L=1 | M_R=0, C_R=0)")
        for step in solution:
            action_or_status = step[0]
            state_after_action = step[1]
            if action_or_status == "Goal Reached":
                 print(f"-> {action_or_status}: {state_after_action}")
            else:
                # The state printed is the state *before* the action was taken.
                # To show the state *after* the action, we need to look ahead or reconstruct.
                # Let's adjust the path storage to make this clearer.
                # The current path stores (action, state_before_action)
                # The final element is (Goal Reached, final_state)
                # Let's re-think the printing loop to be more intuitive.
                pass # Will adjust printing logic below

        # Revised printing logic for clarity
        current_s = State(N_PERSONS, N_PERSONS, 1) # Start with initial state
        print(f"Start: {current_s}")
        for i in range(len(solution) -1): # Exclude the final 'Goal Reached' tuple
            action, _ = solution[i] # Action that led from previous state to next
            # The next state in the sequence is the state *after* this action
            # This is implicitly the `current_state` of the *next* iteration in the BFS queue
            # Or, more directly, the first element of the next tuple in the `solution` list
            # if we stored (action, resulting_state) in path. Let's adjust path storage.
            
            # Re-evaluating path storage in solve_missionaries_cannibals:
            # new_path = path + [(action, current_state)] # current_state is state *before* action
            # queue.append((next_s, new_path)) # next_s is state *after* action
            # So, the path is a list of (action_taken_to_get_to_prev_state, prev_state)
            # The final tuple is ("Goal Reached", goal_state)
            
            # Let's try a simpler path storage: just the sequence of states and actions
            # Path could be [(state0, action1, state1, action2, state2, ... goal_state)]
            # Or, a list of (action, resulting_state) tuples.
            # The current path is a list of (action_that_led_to_state_in_tuple, state_before_that_action)
            # This is a bit confusing for printing. Let's simplify the output process.
            
            # The `solution` list currently looks like:
            # [ (action1, state0), (action2, state1), ..., (action_final, state_N-1), ("Goal Reached", state_N) ]
            # where state0 is initial, state_N is goal.
            # action1 takes state0 to state1.
            # action2 takes state1 to state2.

            action_description = solution[i][0]
            state_before_this_action = solution[i][1]
            # The state *after* this action is the `current_state` of the next element in the path,
            # or the final goal state if it's the last action.
            if i + 1 < len(solution):
                state_after_this_action = solution[i+1][1] # This is the state component of the next path element
            else: # Should not happen if loop is correct
                state_after_this_action = "Error in path structure"

            print(f"Action: {action_description} -> Results in: {state_after_this_action}")
        
        final_status, final_state_obj = solution[-1]
        if final_status != "Goal Reached":
            print("Error: Path did not end with Goal Reached.")


