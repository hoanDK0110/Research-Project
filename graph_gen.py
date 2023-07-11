import networkx as nx
import matplotlib.pyplot as plt
# Thêm các nút và trọng số nút
PHY = nx.Graph()
PHY.add_node("0", weight=5)
PHY.add_node("1", weight=2)
PHY.add_node("2", weight=4)
PHY.add_node("3", weight=1)
PHY.add_node("4", weight=3)
PHY.add_node("5", weight=2)

PHY.add_edge("0", "1", weight=0.6)
PHY.add_edge("0", "2", weight=0.2)
PHY.add_edge("2", "3", weight=0.1)
PHY.add_edge("2", "4", weight=0.7)
PHY.add_edge("2", "5", weight=0.9)
PHY.add_edge("0", "3", weight=0.3)


# Thêm các cạnh và trọng số cạnh
SFC = nx.Graph()
SFC.add_node("0", weight=1)
SFC.add_node("1", weight=2)
SFC.add_node("2", weight=3)

SFC.add_edge("0", "1", weight=0.1)
SFC.add_edge("1", "2", weight=0.2)

nx.write_gml(SFC, "SFC_graph.gml")
nx.write_gml(PHY, "PHY_graph.gml")


nodes_PHY = list(PHY.nodes())


plt.subplot(121)
elarge = [(u, v) for (u, v, d) in PHY.edges(data=True)]
pos = nx.spring_layout(PHY, seed=0)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(PHY, pos, node_size=2000,node_color = "Blue")

# edges
nx.draw_networkx_edges(PHY, pos, edgelist=elarge, width=3)
nx.draw_networkx_edges(PHY, pos)

# node labels
nx.draw_networkx_labels(PHY, pos, font_size=20, font_family="Times new Roman", font_weight="bold", font_color="white")
# edge weight labels
edge_labels = nx.get_edge_attributes(PHY, "weight")
nx.draw_networkx_edge_labels(PHY, pos, edge_labels,font_size=15,font_family="Times new Roman", )

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()

plt.subplot(122)
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


