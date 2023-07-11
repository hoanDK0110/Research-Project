import networkx as nx
import matplotlib.pyplot as plt
import random
PHY = nx.Graph()
node = 10
"""PHY.add_node("0", weight=5)
PHY.add_node("1", weight=2)
PHY.add_node("2", weight=4)
PHY.add_node("3", weight=1)
PHY.add_node("4", weight=3)
PHY.add_node("5", weight=2)

PHY.add_edge("0", "1", weight=6)
PHY.add_edge("0", "2", weight=2)
PHY.add_edge("2", "3", weight=1)
PHY.add_edge("2", "4", weight=7)
PHY.add_edge("2", "5", weight=9)
PHY.add_edge("0", "3", weight=3)"""



# Thêm các node với trọng số ngẫu nhiên từ 1 đến 5

for i in range(node):
    node_name = str(i)
    weight = random.uniform(1, 5)
    PHY.add_node(node_name, weight=weight)

# Thêm các cạnh với trọng số ngẫu nhiên từ 0.1 đến 1
for i in range(node):
    for j in range(i + 1, node):
        edge_weight = random.uniform(0.1, 1)
        PHY.add_edge(str(i), str(j), weight=edge_weight)

nx.write_gml(PHY, "PHY_graph.gml")

#plt.subplot(121)
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
plt.show()