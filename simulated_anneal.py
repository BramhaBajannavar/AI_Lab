import random
import math

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def heuristic(state):
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def random_neighbor(state):
    n = len(state)
    col = random.randint(0, n - 1)
    row = random.randint(0, n - 1)
    while state[col] == row:
        row = random.randint(0, n - 1)
    neighbor = state.copy()
    neighbor[col] = row
    return neighbor

def simulated_annealing(n, initial_temp=100, cooling_rate=0.98, max_steps=1000, log_interval=50):
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_h = heuristic(current)
    temp = initial_temp

    print("Initial State:")
    print_board(current)
    print(f"Heuristic: {current_h}\n")

    for step in range(max_steps):
        if current_h == 0:
            print(f"✅ Solution found at step {step}!")
            break

        neighbor = random_neighbor(current)
        neighbor_h = heuristic(neighbor)
        delta = neighbor_h - current_h

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = neighbor
            current_h = neighbor_h

        temp *= cooling_rate

        if step % log_interval == 0 or current_h == 0:
            print(f"Step {step}:")
            print_board(current)
            print(f"Heuristic: {current_h}, Temperature: {temp:.2f}\n")

    return current, current_h

n = int(input("Enter number of queens (N > 3): "))
solution, h = simulated_annealing(n)

if h != 0:
    print("Failed to find solution. Try again or adjust parameters.")
