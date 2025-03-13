from queue import PriorityQueue
import time

def print_state(state):
    for row in state:
        print(" ".join(str(num) if num != 0 else "_" for num in row))
    print()

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # Cost from start node
        self.h = h  # Heuristic cost
        self.f = g + h  # Total estimated cost
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(state, goal):
    # Manhattan Distance Heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    neighbors = []
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    zero_pos = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
    x, y = zero_pos
    
    for move, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((move, tuple(map(tuple, new_state)), (x, y, nx, ny)))
    
    return neighbors

def a_star(start, goal):
    goal_flat = sum(goal, ())  # Flatten goal state for easy lookup
    start_node = PuzzleNode(start, g=0, h=heuristic(start, goal_flat))
    pq = PriorityQueue()
    pq.put(start_node)
    visited = set()
    
    while not pq.empty():
        current = pq.get()
        visited.add(current.state)
        
        if current.state == goal:
            path = []
            states = []
            while current:
                if current.move:
                    path.append(current.move)
                states.append(current.state)
                current = current.parent
            path.reverse()
            states.reverse()
            return path, states
        
        for move, neighbor, pos in get_neighbors(current.state):
            if neighbor in visited:
                continue
            g_cost = current.g + 1
            h_cost = heuristic(neighbor, goal_flat)
            pq.put(PuzzleNode(neighbor, current, move, g_cost, h_cost))
    
    return None, None  # No solution

start_state = ((1, 2, 3), (4, 0, 5), (6, 7, 8))  # 0 represents the empty tile
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
solution, states = a_star(start_state, goal_state)

if solution:
    print("Starting state:")
    print_state(start_state)
    time.sleep(1)
    print("Solution found:")
    for move, state in zip(solution, states[1:]):
        print(f"Move: {move}")
        print_state(state)
        time.sleep(1)
else:
    print("No solution possible")
