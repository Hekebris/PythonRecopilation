import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()
axel = [('A','F', 8),('A','B', 5),('A','C', 2),('A','B', 5),('B','G', 10),('B','H', 9),('B','K', 7),('C','K', 6),('F','G', 10),('G','I', 7),('H','J', 2),('H','K', 12),('H','I', 6),('I','J', 4),('J','K', 12)]
pos = {'A': (1.5, 4), 'B': (2, 2.5), 'C': (3, 4.5), 'D': (1, 1), 'E': (3, 0.8), 'F': (0.5, 2), 'G': (0, 0), 'H': (3, 1.5), 'I': (3, 0), 'J': (5, 1), 'K': (5, 4)}
grafo.add_weighted_edges_from(axel)
arbolMinimo = nx.minimum_spanning_tree(grafo)

fig, ax = plt.subplots(figsize=(10,8))
nx.draw_networkx(arbolMinimo, pos=pos, with_labels=True, ax=ax, node_color = 'blue', edge_color = 'black', width = 2)
nx.draw_networkx_edge_labels(arbolMinimo, pos=pos, edge_labels=nx.get_edge_attributes(arbolMinimo, 'weight'), ax=ax)

fig, ax = plt.subplots(figsize=(10,8))
nx.draw_networkx(grafo, pos=pos, with_labels=True, ax=ax, node_color = 'purple', edge_color = 'gray', width = 2)  
nx.draw_networkx_edge_labels(grafo, pos=pos, edge_labels=nx.get_edge_attributes(grafo, 'weight'), ax=ax)

plt.show()