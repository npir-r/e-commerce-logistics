"""
E-Commerce Logistics Network Optimization
Network optimization using Minimum Spanning Tree and Shortest Path algorithms
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set font for Turkish characters
rcParams['font.sans-serif'] = ['DejaVu Sans']

# 1. DATA LOADING
print("=" * 60)
print("E-COMMERCE LOGISTICS NETWORK OPTIMIZATION")
print("=" * 60)

# Read CSV file
df = pd.read_csv('../data/network_data.csv')
print("\n📊 Network Data:")
print(df)

# 2. CREATE NETWORK
G = nx.Graph()

# Add nodes (cities)
cities = list(set(df['source'].tolist() + df['target'].tolist()))
G.add_nodes_from(cities)

# Add edges (connections)
for idx, row in df.iterrows():
    G.add_edge(row['source'], row['target'], 
               distance=row['distance'], 
               cost=row['cost'],
               capacity=row['capacity'])

print(f"\n🔗 Network Properties:")
print(f"   Total Nodes: {G.number_of_nodes()}")
print(f"   Total Edges: {G.number_of_edges()}")
print(f"   Is Connected: {nx.is_connected(G)}")

# 3. NODES AND EDGES
print(f"\n📍 Warehouse Centers (Nodes): {sorted(G.nodes())}")
print(f"\n🚚 Connections (Edges):")
for source, target, data in G.edges(data=True):
    print(f"   {source} ↔ {target} | Distance: {data['distance']}km | "
          f"Cost: ₺{data['cost']} | Capacity: {data['capacity']} packages/day")

# 4. MINIMUM SPANNING TREE (Kruskal)
print("\n" + "=" * 60)
print("ALGORITHM 1: MINIMUM SPANNING TREE (Kruskal)")
print("=" * 60)
print("Objective: Connect all centers with minimum cost")

MST = nx.minimum_spanning_tree(G, weight='cost')
mst_edges = list(MST.edges(data=True))
total_mst_cost = sum(data['cost'] for _, _, data in mst_edges)

print(f"\n✅ Minimum Cost Network Found!")
print(f"   Total Edges: {MST.number_of_edges()}")
print(f"   Total Cost: ₺{total_mst_cost}")
print(f"\n📋 Selected Connections:")
for source, target, data in sorted(mst_edges):
    print(f"   {source} → {target} | Cost: ₺{data['cost']}")

# 5. SHORTEST PATH (Dijkstra)
print("\n" + "=" * 60)
print("ALGORITHM 2: SHORTEST PATH (Dijkstra)")
print("=" * 60)
print("Objective: Find shortest distance from Istanbul to Diyarbakir")

try:
    shortest_path = nx.shortest_path(G, source='Istanbul', target='Diyarbakir', weight='distance')
    path_distance = nx.shortest_path_length(G, source='Istanbul', target='Diyarbakir', weight='distance')
    
    print(f"\n✅ Shortest Path Found!")
    print(f"   Route: {' → '.join(shortest_path)}")
    print(f"   Total Distance: {path_distance} km")
    
    # Show path details
    print(f"\n   Path Details:")
    for i in range(len(shortest_path) - 1):
        src = shortest_path[i]
        tgt = shortest_path[i + 1]
        dist = G[src][tgt]['distance']
        cost = G[src][tgt]['cost']
        print(f"      {src} → {tgt} | {dist}km | ₺{cost}")
except nx.NetworkXNoPath:
    print("⚠️ No path found from Istanbul to Diyarbakir!")

# 6. NETWORK STATISTICS
print("\n" + "=" * 60)
print("NETWORK STATISTICS")
print("=" * 60)

# Degree centrality
degree_centrality = nx.degree_centrality(G)
print("\n📊 Most Important Warehouse Centers (by connections):")
for city, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f"   {city}: {centrality:.2f}")

# Average distance
avg_distance = sum(data['distance'] for _, _, data in G.edges(data=True)) / G.number_of_edges()
print(f"\n📏 Average Connection Distance: {avg_distance:.1f} km")

# Total cost
total_cost = sum(data['cost'] for _, _, data in G.edges(data=True))
print(f"💰 Total Network Cost (All connections): ₺{total_cost}")

# Total capacity
total_capacity = sum(data['capacity'] for _, _, data in G.edges(data=True))
print(f"📦 Total Network Capacity: {total_capacity} packages/day")

# 7. VISUALIZATION
print("\n" + "=" * 60)
print("CREATING VISUALIZATIONS...")
print("=" * 60)

plt.figure(figsize=(14, 10))

# Network layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='#FF6B6B', 
                       node_size=2000, alpha=0.9)

# Draw edges
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='#4ECDC4')

# Add labels
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

# Edge labels (distance)
edge_labels = {(u, v): f"{d['distance']}km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

plt.title('E-Commerce Logistics Network - Warehouse Centers and Connections', 
          fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('../results/network_visualization.png', dpi=300, bbox_inches='tight')
print("✅ Network visualization saved: network_visualization.png")

# MST Visualization
plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(MST, pos, node_color='#95E1D3', 
                       node_size=2000, alpha=0.9)
nx.draw_networkx_edges(MST, pos, width=3, alpha=0.8, edge_color='#F38181')
nx.draw_networkx_labels(MST, pos, font_size=9, font_weight='bold')

mst_labels = {(u, v): f"₺{d['cost']}" for u, v, d in MST.edges(data=True)}
nx.draw_networkx_edge_labels(MST, pos, mst_labels, font_size=8)

plt.title('Minimum Spanning Tree (MST) - Optimal Network with Minimum Cost', 
          fontsize=14, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.savefig('../results/mst_visualization.png', dpi=300, bbox_inches='tight')
print("✅ MST visualization saved: mst_visualization.png")

print("\n" + "=" * 60)
print("✅ PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 60)
