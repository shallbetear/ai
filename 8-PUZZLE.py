def misplaced_tiles(state, goal):
    return sum(s != g and s != 0 for s, g in zip(state, goal))

def get_neighbors(state):
    neighbors=[] 
    i = state.index(0)
    swap = lambda a, b: (state[a],) + (state[b],) + state[:a] + state[a+1:b] + state[b+1:]
    if i % 3 > 0: neighbors.append(swap(i, i - 1))
    if i % 3 < 2: neighbors.append(swap(i, i + 1))
    if i // 3 > 0: neighbors.append(swap(i, i - 3))
    if i // 3 < 2: neighbors.append(swap(i, i + 3))
    return neighbors

def hill_climbing(state, goal):
    current_state = state
    while (cost := misplaced_tiles(current_state, goal)) > 0:
        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=lambda s: misplaced_tiles(s, goal))
        next_cost = misplaced_tiles(next_state, goal)
        if next_cost >= cost:
            break
        current_state = next_state
    return current_state

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

initial = (3, 2, 7, 6, 8, 1, 5, 4, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = hill_climbing(initial, goal)

print("Initial State:")
print_state(initial)
print("Solution State:")
print_state(solution)
