"""
    This is just a sample function for us to visualise the helper classes created.
"""
def main():
    graph = Graph()
    print("Name: " + str(graph.fetch_current_node().fetch_location_name()))
    print("Type: " + str(graph.fetch_current_node().fetch_location_type()))
    print("Neighbors: ")
    for node in graph.fetch_current_node().fetch_neighbors():
        print(node.to_string())
    print("Edge Mapping:")
    print(graph.fetch_edge_mapping().to_string())

"""
    Creating a custom node definition in order to store the following data.
        1) Name of the Location.
        2) Type of Location.
        3) Neighbors or Adjacent Locations - Using an Adjacency list.
"""
class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.neighbors = []
    
    def fetch_location_name(self):
        return self.name
    
    def fetch_location_type(self):
        return self.type

    def fetch_neighbors(self):
        return self.neighbors
    
    def add_neighbor(self, node):
        self.neighbors.append(node)
    
    def add_neighbors(self, nodes):
        self.neighbors.extend(nodes)
    
    def to_string(self):
        return "Name: " + str(self.name) + " Type: " + self.type.to_string() + " Neighbors: " + str(self.neighbors)

"""
    Creating an enum to track the type of location. 
    As of now, there are only 2 types of locations: 
        1) Dull - There is nothing to do here.
        2) Vibrant - There is a lot to do here.
"""
from enum import Enum
class LocationType(Enum):
    START = "Start"
    DULL = "Dull"
    VIBRANT = "Vibrant"

    def to_string(self):
        return str(self.value)

"""
    Creating a class for Graph which will instantiate and set up the graph our hitch-hiker will navigate.
"""
import random
class Graph:
    node_number_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    
    def __init__(self):
        # Creating the start node where our hitch-hiker resides.
        self.current_node = Node("A", LocationType.START)
        self.edge_mapping = Edge(5)

        # Temporary Nodes to test the concept.
        B = Node("B", LocationType.VIBRANT)
        C = Node("C", LocationType.DULL)
        D = Node("D", LocationType.VIBRANT)
        E = Node("E", LocationType.DULL)

        for node in [B, C, D, E]:
            self.current_node.add_neighbor(node)
            self.edge_mapping.add_edge(self.node_number_mapping[self.current_node.fetch_location_name()], self.node_number_mapping[node.fetch_location_name()], random.randint(1, 10))
    
    def fetch_current_node(self):
        return self.current_node

    def fetch_edge_mapping(self):
        return self.edge_mapping

"""
    Creating a class for Edge which will keep track of the cost of traveling from one node to another.
    It is just a database of all the nodes and gives us the ability to fetch the cost of traveling from one node to another.
    As of now, it is a simple cost. It must change in the future to incorporate the cost of traveling from one node to another with different properties.
"""
class Edge:
    def __init__(self, size):
        # Keeps track of the length of row or column in an nxn matrix.
        self.size = size
        self.edges = [[-float("inf") for i in range(size)] for j in range(size)]
    
    def add_edge(self, node1, node2, cost):
        self.edges[node1][node2] = cost
        ### As of now, we are maintaining a symmetric matrix. We can change this in the future.
        self.edges[node2][node1] = cost
    
    def fetch_cost(self, node1, node2):
        return self.edges[node1][node2]
    
    def to_string(self):
        return str(self.edges)

if __name__ == "__main__":
    main()