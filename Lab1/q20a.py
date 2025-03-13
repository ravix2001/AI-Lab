# WAP to represent the following graphs using a dictionary

graph = {"A" : ["B", "C"],
         "B" : ["A", "D", "E"],
         "C" : ["A", "F"],
         "D" : ["B", "G"],
         "E" : ["B", "H"],
         "F" : ["C"],
         "G" : ["D"],
         "H" : ["E"]
         }

print("Graph is ",graph)

# to find the path

def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 


print("Path is ",find_path(graph, 'H', 'F'))