from collections import deque

def bfs(start, goal):
    visited, queue = set(), deque([(start, [])])
    while queue:
        state, path = queue.popleft()
        if state == goal: return path + [state]
        visited.add(state)
        i = state.index(0)
        for move in [-3, 3, -1, 1]:
            ni = i + move
            if 0 <= ni < 9 and (i % 3 != 0 or move != -1) and (i % 3 != 2 or move != 1):
                new = list(state)
                new[i], new[ni] = new[ni], new[i]
                tnew = tuple(new)
                if tnew not in visited:
                    queue.append((tnew, path + [state]))
    return None

start = (1, 2, 3, 4, 5, 6, 0, 7, 8)
goal = tuple(map(int, input("Enter goal state (9 numbers, space-separated): ").split()))
path = bfs(start, goal)

if path:
    for step, state in enumerate(path):
        print(f"\nStep {step}:")
        for i in range(0, 9, 3): print(state[i:i+3])
else:
    print("No solution found.")
