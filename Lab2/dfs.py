import pprint

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
 
def DFS(G, start, goal):
    # initialize a stack
    stack = list()
    # initialize a dictionary to store the previous node of the current node
    prev = dict()
    # initialize a set to store the visited nodes
    visited = set()
    stack.append(start)
    prev[start] = " "
    while(stack):
        poppedState = stack.pop()
        # mark the poppedstate 
        visited.add(poppedState)
        # return if popped state is goal
        if poppedState == goal:
            return True, prev
        # push all the chhimekis of poppedState if they are not already in the stack and not already visited
        for chhimeki in G[poppedState]:
            if chhimeki not in stack and chhimeki not in visited:
                stack.append(chhimeki)
                prev[chhimeki] = poppedState
    return False, prev

def reconstruct_path(G, previous, goal):
    path = goal
    while(previous[goal] != ' '):
        path = previous[goal]+ '->' +path
        goal = previous[goal]
    return path

def computeCost(solutionPath):
    cost = 0
    for i in range(len(solutionPath)-1):
        cost += G[solutionPath[i]][solutionPath[i+1]]
    return cost

start = "biratnagar"
goal = "damak"
goalFound, previous =  DFS(G, start, goal)
if(goalFound):
    pprint.pprint(reconstruct_path(G, previous, goal))
    print(computeCost(reconstruct_path(G, previous, goal).split("->")))
else:
    print("No solution")
