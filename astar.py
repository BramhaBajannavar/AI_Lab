import heapq

# Manhattan distance heuristic
def manhattan(state, goal):
    distance = 0
    for i in range(1, 9):  # skip 0 (blank)
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = state.copy()
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(new_state)
    return neighbors

def a_star(start, goal):
    frontier = []
    heapq.heappush(frontier, (manhattan(start, goal), 0, start, []))
    visited = set()

    while frontier:
        est_total, cost, current, path = heapq.heappop(frontier)
        state_tuple = tuple(current)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                new_cost = cost + 1
                est = new_cost + manhattan(neighbor, goal)
                heapq.heappush(frontier, (est, new_cost, neighbor, path + [current]))

    return None

start = list(map(int, input("Enter start state (e.g. 1 2 3 4 5 6 7 8 0): ").split()))
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution_path = a_star(start, goal)

if solution_path:
    print(f"\nSolution found in {len(solution_path) - 1} moves:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found.")