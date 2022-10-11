import matplotlib.pyplot as plt
import networkx as nx
import warnings

n = 200  # number nodes
p = 0.25  # number edges
            # Is there a possibility to enter to specify the edge probability? As far as I understood the property of the 
            # of the erdos reny graph is that all graphs with n nodes and m edges are equally likely. Therefore, does it then 
            # make sense that Amelkin et.al. specify an edge probability?
            # similar with p probability for edges - then edge number stays unsatisfied  https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnp_random_graph.html#networkx.generators.random_graphs.gnp_random_graph
seed = 2022  # seed random number generators for reproducibility

# Use seed for reproducibility
G_is_strongly_connected = False
for i in range(100):
    G = nx.gnp_random_graph(n, p, seed=seed, directed=True)
    if nx.is_strongly_connected(G):
        G_is_strongly_connected = True
        break

print('Graph is strongly connected:')
print(G_is_strongly_connected)

# throw exception if now strongly connected graph was found
if not G_is_strongly_connected:
        warnings.warn("No strongly conected erdos reny graph could be determined.")

# determine adjacency matrix 
adj_matrix = (nx.adjacency_matrix(G, weight="None")).todense()

print(adj_matrix)


pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout
nx.draw(G, pos=pos)
plt.show()