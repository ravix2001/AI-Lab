from queue import PriorityQueue

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
            neighbors.append((move, tuple(map(tuple, new_state))))
    
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
            while current.parent:
                path.append(current.move)
                current = current.parent
            return path[::-1]
        
        for move, neighbor in get_neighbors(current.state):
            if neighbor in visited:
                continue
            g_cost = current.g + 1
            h_cost = heuristic(neighbor, goal_flat)
            pq.put(PuzzleNode(neighbor, current, move, g_cost, h_cost))
    
    return None  # No solution

# Example usage
start_state = ((1, 2, 3), (4, 0, 5), (6, 7, 8))  # 0 represents the empty tile
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
solution = a_star(start_state, goal_state)

if solution:
    print("Solution found:", solution)
else:
    print("No solution possible")
