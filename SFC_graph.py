import networkx as nx
import matplotlib.pyplot as plt
import random
SFC = nx.Graph()
SFC.add_node("0", weight=1)
SFC.add_node("1", weight=2)
SFC.add_node("2", weight=2)
SFC.add_node("3", weight=3)

SFC.add_edge("0", "1", weight=0.1)
SFC.add_edge("1", "2", weight=0.2)
SFC.add_edge("2", "3", weight=0.2)

nx.write_gml(SFC, "SFC_graph.gml")

#plt.subplot(122)
elarge = [(u, v) for (u, v, d) in SFC.edges(data=True)]
pos = nx.spring_layout(SFC, seed=0)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(SFC, pos, node_size=2000,node_color = "Blue")

# edges
nx.draw_networkx_edges(SFC, pos, edgelist=elarge, width=3)
nx.draw_networkx_edges(SFC, pos)

# node labels
nx.draw_networkx_labels(SFC, pos, font_size=20, font_family="Times new Roman", font_weight="bold", font_color="white")
# edge weight labels
edge_labels = nx.get_edge_attributes(SFC, "weight")
nx.draw_networkx_edge_labels(SFC, pos, edge_labels,font_size=15,font_family="Times new Roman", )

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()