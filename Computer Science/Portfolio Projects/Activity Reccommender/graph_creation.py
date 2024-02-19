from activity_data import activity_categories
import networkx as nx
import matplotlib.pyplot as plt
class Vertex: 
    def __init__(self,value):
        self.value = value
        self.edges = {}
    
    def add_edge(self,vertex, weight = 0):
        self.edges[vertex] = weight
    
    def get_edges(self):
        return list(self.edges.keys())
    
class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self,vertex): 
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
    def return_nodes(self):
        return list(self.graph_dict.keys())
    def search(self, interest_list, lim):
        check_dict = {}
        check_list = []
        RList = []
        first_key = next(iter(self.graph_dict))  # Get the first key
        start_vertex = self.graph_dict[first_key]
        for mood_interest_key  in start_vertex.get_edges():
            mood_interest = self.graph_dict[mood_interest_key]
            if mood_interest.value in interest_list:
                for activity in mood_interest.get_edges(): 
                    check_list.append(activity)

        for activity_key in check_list[1:]:
            activity = self.graph_dict[activity_key]
            int_count = 0
            for edge in activity.get_edges():
                if edge in interest_list:
                    int_count += 1
            check_dict[activity.value] = int_count
        
        return check_dict
    


#create the graph
activity_graph = Graph(directed = False)  
starting_vert = Vertex("Start")
activity_graph.add_vertex(starting_vert)
mood_interest_vertices = {}
mood_interest_vertices["Start"] = starting_vert
# populate the graph data structure using the AI generated activity_categories python dictionary
for mood_interest in activity_categories.keys():
    vertex = Vertex(mood_interest)
    activity_graph.add_vertex(vertex)
    activity_graph.add_edge(starting_vert, vertex)
    mood_interest_vertices[mood_interest] = vertex

activity_vertices = {}
for activities in activity_categories.values():
    for activity in activities:
        if activity not in activity_vertices:
            vertex = Vertex(activity)
            activity_graph.add_vertex(vertex)
            activity_vertices[activity] = vertex


for mood_interest, activities in activity_categories.items():
    mood_interest_vertex = mood_interest_vertices[mood_interest]
    for activity in activities:
        activity_vertex = activity_vertices[activity]
        activity_graph.add_edge(mood_interest_vertex, activity_vertex)



#print(activity_graph.return_nodes())
""" 
print("Mood/Interest Vertices:")
for vertex in mood_interest_vertices.values():
    print(vertex.value, vertex.get_edges())

print("\nActivity Vertices:")
for vertex in activity_vertices.values():
    print(vertex.value, vertex.get_edges())

# 2. Check Edges
print("\nEdges:")
for vertex in mood_interest_vertices.values():
    for neighbor in vertex.get_edges():
        print(f"{vertex.value} -> {neighbor}")

G = nx.Graph()
for vertex in mood_interest_vertices.values():
    G.add_node(vertex.value)
for vertex in activity_vertices.values():
    G.add_node(vertex.value)
for vertex in mood_interest_vertices.values():
    for neighbor in vertex.get_edges():
        G.add_edge(vertex.value, neighbor)
pos = nx.spring_layout(G)

nx.draw(G, with_labels=True, node_size=200, font_size=5)  # Adjust node size and font size as needed
plt.show()
# """