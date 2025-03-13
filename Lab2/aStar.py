from pprint import pprint
from queue import PriorityQueue

G = {
 'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
 'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
 'dharan' : {'itahari' : 20},
 'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10}, 
 'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40}, 
 'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
 'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
 'damak' : {'urlabari' : 6}
}

h = {
 'biratnagar' : 46,
 'itahari' : 39,
 'dharan' : 41,
 'rangeli' : 28,
 'biratchowk' : 29,
 'kanepokhari' : 17,
 'urlabari' : 6,
 'damak' : 0
}

def astar(G ,h, start, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited =set()
    # enque the initial state into the priority queue
    # we use format (fscore, (state, gScore))
    PQ.put((0+h[start], (start,0)))
    # we set the prev of start to " "
    prev[start] = " "
    # repeat until the priority queue is not empty
    while(not PQ.empty()):
        # dequeue
        outStateFScore, (outState, outStateGScore) = PQ.get()
        # mark it as visited
        visited.add(outState)
        # if the outstate is in the goal state then return
        if outState == goal:
            return True, prev, outStateFScore
        for chhimeki in G[outState]:
            if chhimeki not in visited:
                chhimekiGScore = outStateGScore + G[outState][chhimeki]
                PQ.put((chhimekiGScore+h[chhimeki], (chhimeki, chhimekiGScore)))
                prev[chhimeki] = outState
    return False, prev, -1

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + " -> "+ path
        goal = previous[goal]
    return path

def computeCost(solutionPath):
    cost = 0
    for i in range(len(solutionPath)-1):
        cost += G
    return cost


start = "biratnagar"
goal = "damak"
goalFound, previous, cost = astar(G, h, start, goal)
if(goalFound):
    print(reconstruct_path(G, previous, goal))
    print("Cost = ", cost)
else:
    print("No solution")
