import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost  # g(n) + h(n)

    def __lt__(self, other):
        return self.cost < other.cost

    def find_blank(self):
        return self.state.index(0)

    def generate_children(self):
        children = []
        idx = self.find_blank()
        x, y = divmod(idx, 3)
        directions = {
            'Up': (x - 1, y),
            'Down': (x + 1, y),
            'Left': (x, y - 1),
            'Right': (x, y + 1),
        }
        for move, (nx, ny) in directions.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_idx = nx * 3 + ny
                new_state = self.state[:]
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                child = PuzzleNode(new_state, self, move, self.depth + 1)
                children.append(child)
        return children

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  # 1 to 8
        xi, yi = divmod(state.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        distance += abs(xi - xg) + abs(yi - yg)
    return distance

def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    return path[::-1]

def a_star_search(start_state, goal_state):
    open_list = []
    closed_set = set()
    start_node = PuzzleNode(start_state)
    start_node.cost = manhattan_distance(start_state, goal_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(tuple(current_node.state))

        for child in current_node.generate_children():
            if tuple(child.state) in closed_set:
                continue
            g = current_node.depth + 1
            h = manhattan_distance(child.state, goal_state)
            child.cost = g + h
            heapq.heappush(open_list, child)

    return None
if __name__ == "__main__":
    start = [1, 2, 3,
             4, 0, 5,
             7, 8, 6]

    goal = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

    solution = a_star_search(start, goal)
    if solution:
        print("Steps to solve:", solution)
        print("Number of moves:", len(solution))
    else:
        print("No solution found.")
