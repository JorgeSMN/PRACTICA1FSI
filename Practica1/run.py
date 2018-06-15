# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
cd = search.GPSProblem('C', 'D', search.romania)
ef= search.GPSProblem('E', 'F', search.romania)
gh= search.GPSProblem('G', 'H', search.romania)

"""
print search.breadth_first_graph_search(ab).path() #anchura
print search.depth_first_graph_search(ab).path() #profundidad
print search.iterative_deepening_search(ab).path()
print search.depth_limited_search(ab).path()
"""
print search.ramificacion_search(ab).path()#ramificacion
print search.ramificacion_subestimacion_search(ab).path()#ramificacion
print "----------------------------------------------"
print search.ramificacion_search(cd).path()#ramificacion
print search.ramificacion_subestimacion_search(cd).path()#ramificacion
print "----------------------------------------------"
print search.ramificacion_search(ef).path()#ramificacion
print search.ramificacion_subestimacion_search(ef).path()#ramificacion
print "----------------------------------------------"
print search.ramificacion_search(gh).path()#ramificacion
print search.ramificacion_subestimacion_search(gh).path()#ramificacion

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
