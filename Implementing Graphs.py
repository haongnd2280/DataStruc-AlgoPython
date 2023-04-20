# Graphs are easily built out of lists and dictionaries. 

graph = {'A': ['B', 'C'],   # this is directed graph using dictionary. 
         'B': ['C', 'D'], 
         'C': ['D'], 
         'D': ['C'], 
         'E': ['F'], 
         'F': ['C']} 

# Let's write a simple function to determine a path between two nodes. 
# This function won't contain cycles, so the same node will not occur more than once on the path returned. 
# The algorithm uses backtracking: tries each posibility in turn until finds a solution. 

def find_path(graph, start, end, path=[]): 
    path = path + [start]    # create a new list. 
    if start == end: 
        return path 
    if not graph.has_key(start): # necessary only in case there are nodes that are listed as end points for arcs but that don't have outgoing arcs themselves, and aren't listed in the graph at all. Such nodes could also be contained in the graph, with an empty list of outgoing arcs, but sometimes it is more convenient not to require this.
        return None   
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: return newpath   # if newpath is not False. 
    
    return None  

find_path(graph, 'A', 'D')