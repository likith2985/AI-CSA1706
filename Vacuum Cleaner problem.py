"""
This program simulates a simple reflex vacuum cleaner agent in a two-room environment.

Environment:
- Two rooms: A and B.
- Each room can be Clean or Dirty.

Agent Actions:
- SUCK: Clean the current room.
- MOVE_TO_A: Move to Room A (if not already there).
- MOVE_TO_B: Move to Room B (if not already there).
- NO_OP: Do nothing (if the environment is clean).

Agent Percepts:
- (location, status): e.g., ('A', 'Dirty')

Agent Logic (Simple Reflex Agent):
- If current location is Dirty, SUCK.
- If current location is Clean and it's Room A, MOVE_TO_B.
- If current location is Clean and it's Room B, MOVE_TO_A.
- If both rooms are clean, NO_OP.
"""

import random

class VacuumEnvironment:
    def __init__(self, room_a_status="Dirty", room_b_status="Dirty"):
        # Possible statuses: "Clean", "Dirty"
        self.rooms = {
            "A": room_a_status,
            "B": room_b_status
        }
        self.agent_location = random.choice(["A", "B"])
        self.performance_score = 0
        print(f"Initial Environment: Room A is {self.rooms['A']}, Room B is {self.rooms['B']}. Agent starts in Room {self.agent_location}.")

    def get_percept(self):
        return (self.agent_location, self.rooms[self.agent_location])

    def is_dirty(self, room):
        return self.rooms[room] == "Dirty"

    def all_clean(self):
        return self.rooms["A"] == "Clean" and self.rooms["B"] == "Clean"

    def step(self, action):
        self.performance_score -= 1 # Cost for each action/time step

        if action == "SUCK":
            if self.rooms[self.agent_location] == "Dirty":
                self.rooms[self.agent_location] = "Clean"
                self.performance_score += 10 # Reward for cleaning
                print(f"Action: SUCK. Room {self.agent_location} is now Clean. Score: {self.performance_score}")
            else:
                print(f"Action: SUCK (but Room {self.agent_location} was already Clean). Score: {self.performance_score}")
        elif action == "MOVE_TO_A":
            if self.agent_location == "B":
                self.agent_location = "A"
                print(f"Action: MOVE_TO_A. Agent is now in Room A. Score: {self.performance_score}")
            else:
                print(f"Action: MOVE_TO_A (but agent already in Room A). Score: {self.performance_score}")
        elif action == "MOVE_TO_B":
            if self.agent_location == "A":
                self.agent_location = "B"
                print(f"Action: MOVE_TO_B. Agent is now in Room B. Score: {self.performance_score}")
            else:
                print(f"Action: MOVE_TO_B (but agent already in Room B). Score: {self.performance_score}")
        elif action == "NO_OP":
             print(f"Action: NO_OP. Environment is clean. Score: {self.performance_score}")
        else:
            print(f"Action: {action} (Unknown action). Score: {self.performance_score}")
        
        print(f"Current State: Room A: {self.rooms['A']}, Room B: {self.rooms['B']}, Agent in: {self.agent_location}")
        return self.get_percept()

class ReflexVacuumAgent:
    def __init__(self):
        pass

    def get_action(self, percept):
        location, status = percept
        if status == "Dirty":
            return "SUCK"
        elif location == "A":
            return "MOVE_TO_B"
        elif location == "B":
            return "MOVE_TO_A"
        return "NO_OP" # Should not be reached if logic is correct and env not all clean


if __name__ == "__main__":
    # Initialize environment with random initial states for rooms
    initial_room_a = random.choice(["Clean", "Dirty"])
    initial_room_b = random.choice(["Clean", "Dirty"])
    env = VacuumEnvironment(room_a_status=initial_room_a, room_b_status=initial_room_b)
    agent = ReflexVacuumAgent()

    max_steps = 10 # Prevent infinite loops for simple agents
    print("\nStarting simulation...")
    for i in range(max_steps):
        if env.all_clean():
            print(f"\nEnvironment is clean after {i} steps.")
            env.step("NO_OP") # One final NO_OP to reflect clean state
            break
        
        print(f"\nStep {i + 1}")
        current_percept = env.get_percept()
        print(f"Agent Percept: {current_percept}")
        action = agent.get_action(current_percept)
        env.step(action)
    
    if not env.all_clean() and i == max_steps -1:
        print(f"\nSimulation ended after {max_steps} steps. Environment may not be fully clean.")
    
    print(f"\nFinal Performance Score: {env.performance_score}")
    print(f"Final State: Room A: {env.rooms['A']}, Room B: {env.rooms['B']}, Agent in: {env.agent_location}")


