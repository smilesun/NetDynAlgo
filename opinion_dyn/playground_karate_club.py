import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from sklearn.preprocessing import normalize

G = nx.karate_club_graph()

arr_w = nx.adj_matrix(G.to_directed()).toarray()

arr_w = normalize(arr_w, axis=1, norm='l1')

arr_w.sum(axis=1) == 1

arr_laplacian = np.eye(arr_w.shape[0]) - arr_w

print("Node Degree")
for v in G:
    print(f"{v:4} {G.degree(v):6}")

nx.draw_circular(G, with_labels=True)
plt.show()
