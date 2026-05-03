# e-commerce-logistics
E-Commerce Logistics Network Optimization
# 1. Real-World Problem Context

Problem Definition
An e-commerce company operating in Turkey wants to efficiently connect its warehouse centers. Currently, there are 9 main warehouse centers, and cargo distribution is carried out between these centers.

Cost Challenge:
Each connection has different costs
Unnecessary costs are incurred to connect all centers
Cargo distribution routes are not optimal

Solutions Needed:
Connect all centers with minimum cost
Find the shortest distance between two centers
Optimize network structure to reduce operational costs


# 2. Problem Definition (Detailed)
Current Situation
Warehouse Centers: Istanbul, Ankara, Izmir, Bursa, Kayseri, Gaziantep, Diyarbakir, Antalya
Number of Routes: 10 routes
Total Network Cost: ₺22,800 (all connections)

Optimization Objectives
Cost Minimization: Using Minimum Spanning Tree algorithm
Route Optimization: Using Shortest Path algorithm
Network Efficiency: Using centrality analysis


# 3. Network Model
Network Type
Undirected Graph: Cargo can be transported in both directions
Weighted Graph: Each connection has different weights (cost, distance, capacity)

Nodes (Vertices) - Warehouse Centers
1. Istanbul       (Hub - Most important center)
2. Ankara         (Regional center)
3. Izmir          (Western region)
4. Bursa          (Northwest)
5. Kayseri        (Central Anatolia)
6. Gaziantep      (Southeast)
7. Diyarbakir     (East)
8. Antalya        (Mediterranean)
Edges (Connections) and Weights
SourceTargetDistance (km)Cost (₺)Capacity (packages/day)IstanbulAnkara4502,250500IstanbulIzmir5602,800400AnkaraGaziantep6503,250350AnkaraKayseri3201,600450IzmirAntalya4802,400300GaziantepDiyarbakir3801,900280KayseriDiyarbakir5202,600350AntalyaIstanbul6003,000350IstanbulBursa2401,200550BursaAnkara3601,800400

# 4. Nodes and Edges

Network Properties
Number of Nodes: 8
Number of Edges: 10
Network Connectivity: Fully connected
Graph Type: Undirected Weighted Graph

Connection Analysis
Minimum Cost Connection: Istanbul-Bursa (₺1,200)
Maximum Cost Connection: Ankara-Gaziantep (₺3,250)
Shortest Distance: Istanbul-Bursa (240 km)
Longest Distance: Ankara-Gaziantep (650 km)

# 5. Selected Algorithm: Minimum Spanning Tree (Kruskal)

Why MST Algorithm?
MST algorithm was selected because:
Most suitable for cost minimization
Connects all warehouse centers with minimum cost
Eliminates unnecessary connections
Reduces operational costs

How Kruskal's Algorithm Works
Sort all edges by cost (smallest to largest)
Add edges to the network in order
Select edges that do not create cycles
Continue until all nodes are connected

Results
Optimal Network (MST):

Istanbul → Bursa (₺1,200)
Bursa → Ankara (₺1,800)
Ankara → Kayseri (₺1,600)
Gaziantep → Diyarbakir (₺1,900)
Kayseri → Diyarbakir (₺2,600)
Izmir → Antalya (₺2,400)
Istanbul → Ankara (₺2,250)

Total Cost: ₺14,300
Savings: ₺22,800 - ₺14,300 = ₺8,500 (37.3% cost reduction!)

# 6. Python Implementation
Libraries Used

NetworkX: Network analysis and algorithms
Pandas: Data management
Matplotlib: Visualization

Main Steps
python1. Data loading (from CSV)
2. Network creation
3. Minimum Spanning Tree calculation
4. Shortest path finding
5. Network statistics
6. Visualization
Core Code Structure
python# Import libraries
import networkx as nx
import pandas as pd

# Load data
df = pd.read_csv('network_data.csv')

# Create network
G = nx.Graph()
# Add nodes and edges...

# Calculate MST
MST = nx.minimum_spanning_tree(G, weight='cost')

# Find shortest path
path = nx.shortest_path(G, 'Istanbul', 'Diyarbakir', weight='distance')

# 7. Results (Output)
MST Optimization Results
✅ Minimum Cost Network Found!
   Total Number of Edges: 7
   Total Cost: ₺14,300
   Cost Reduction Rate: 37.3%
Shortest Path Found
Istanbul → Ankara → Kayseri → Diyarbakir
Total Distance: 1,290 km
Network Characteristics

Connection Count (Degree):

Istanbul: 3 (hub center)
Ankara: 3 (main center)
Others: 1-2 average


Average Distance: 446.5 km
Average Cost: ₺2,280


# 8. Managerial Interpretation
Strategic Recommendations
1. Cost Savings

Implementing MST can save ₺8,500 per period
This reduces operational costs by 37.3%
Annual savings potential: ₺102,000

2. Network Structure Proposal

Use Istanbul and Ankara as hub centers
Make Bursa, Kayseri, and Gaziantep regional centers
Connect other cities to these centers

3. Route Optimization

For Diyarbakir shipments, use the 1,290 km route
Suggest highway and railway combination
Mediterranean route benefits for Izmir-Antalya

4. Capacity Planning

Istanbul: Daily capacity of 1,450 packages (Hub)
Ankara: Daily capacity of 1,250 packages
Others: 280-550 packages average

5. Risk Management
Create backup routes due to increased importance of Istanbul and Ankara
Plan alternative network for natural disaster scenarios


# 9. How to Run the Code
System Requirements
Python 3.7 or higher
pip package manager

Installation Steps

Navigate to project folder:
bash   cd e-commerce-logistics

Install dependencies:
bash   pip install -r requirements.txt

Run the code:
bash   python solution.py

Check outputs:
network_visualization.png - Network graph
mst_visualization.png - Optimal network graph
Detailed results in console output



Expected Output
============================================================
E-COMMERCE LOGISTICS NETWORK OPTIMIZATION
============================================================

📊 Network Data:
[10 rows, 5 columns data]

🔗 Network Properties:
   Total Number of Nodes: 8
   Total Number of Edges: 10
   Is Network Connected: True

✅ PROJECT COMPLETED SUCCESSFULLY!
============================================================

# 10. References
Academic Sources

Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs." Numerische mathematik, 1(1), 269-271.
Kruskal, J. B. (1956). "On the shortest spanning subtree of a graph and the traveling salesman problem." Proceedings of the American Mathematical society, 7(1), 48-50.

Technical Resources

NetworkX Documentation: https://networkx.org/documentation/stable/
Python Pandas Tutorial: https://pandas.pydata.org/docs/
Matplotlib Visualization Guide: https://matplotlib.org/stable/contents.html

Business Management

Chopra, S., & Meindl, P. (2016). "Supply Chain Management: Strategy, Planning, and Operation." Pearson Education.
Simchi-Levi, D., Kaminsky, P., & Simchi-Levi, E. (2008). "Designing and Managing the Supply Chain: Concepts, Strategies and Case Studies." McGraw-Hill.

MIS (Management Information Systems) Application

Laudon, K. C., & Laudon, J. P. (2020). "Management Information Systems: Managing the Digital Firm." Pearson.
Turban, E., Volonino, L., & Wood, G. R. (2015). "Information Technology for Management: Advancing Sustainable, Profitable Business Growth."


Project Structure
e-commerce-logistics/
│
├── data/
│   └── network_data.csv              # Network data
│
├── src/
│   └── solution.py                   # Main Python solution
│
├── results/
│   ├── network_visualization.png     # Original network graph
│   └── mst_visualization.png         # MST graph
│
├── notebooks/
│   └── analysis.ipynb               # Jupyter notebook analysis
│
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
│
└── references/
    └── references.md                # Detailed references

License
This project is developed for educational purposes.

Versiyon: 1.0
