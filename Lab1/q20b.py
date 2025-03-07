# WAP to represent the following graphs using a dictionary

graph = { "BIRATNAGAR" : {"RANGELI" : 25, "BIRATCHOWK" : 30, "ITAHARI" : 22},
          "RANGELI" : {"BIRATNAGAR" : 25, "KANEPOKHARI" : 25, "URLABARI" : 40},
          "ITAHARI" : {"BIRATNAGAR" : 22, "BIRATCHOWK" : 11, "DHARAN" : 20},
          "BIRATCHOWK" : {"BIRATNAGAR" : 30, "ITAHARI" : 11, "KANEPOKHARI" : 10},
          "KANEPOKHARI" : {"RANGELI" : 25, "BIRATCHOWK" : 10, "URLABARI" : 12},
          "URLABARI" : {"RANGELI" : 40, "KANEPOKHARI" : 12, "DAMAK"  : 6},
          "DAMAK" : {"URLABARI" : 6},
          "DHARAN" : {"ITAHARI" : 20}
        }

print(graph)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath

print("Path is : ")
print(find_path(graph, 'BIRATNAGAR', 'URLABARI'))
