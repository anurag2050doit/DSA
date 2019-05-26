from random import choice

"""
Bellman–Ford Algorithm
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph.
The graph may contain negative weight edges.

GFG: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
"""


class Vertex:
    """Vertex definition"""

    def __init__(self, value):
        self.name = value
        self.points_to = {}

    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight

    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.name

    def get_neighbour(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()

    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]

    def does_it_point_to(self, key):
        """Return True if this vertex points to dest."""
        return key in self.points_to


class Graph:
    """Graph Structure"""

    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}

    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())

    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def print(self):
        for vertex, edges in self.vertices.items():
            print('Vertex > ', vertex)
            for neighbour in edges.get_neighbour():
                print('Neighbour vertex: ', neighbour.name, 'Weight: ', edges.get_weight(neighbour))


def bellman_ford(graph, src_vertex):
    """
    This will return a dictionary distance
    :param graph: graph object
    :param src_vertex: src_vertex
    :return: distance where distance[v] is min distance from source to v
    """

    distance = dict.fromkeys(graph, float('inf'))

    distance[src_vertex] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbour_vertex in vertex.get_neighbour():
                distance[neighbour_vertex] = min(
                    distance[neighbour_vertex], distance[vertex] + vertex.get_weight(neighbour_vertex)
                )

    return distance


if __name__ == '__main__':
    graph_obj = Graph()

    # Add Vertex to graph
    number_of_vertex = 5
    vertex_list = [i for i in range(1, number_of_vertex)]
    for i in vertex_list:
        graph_obj.add_vertex(str(i))

    weights = range(1, 20)
    for i in weights:
        graph_obj.add_edge(str(choice(vertex_list)), str(choice(vertex_list)), choice(weights))

    graph_obj.print()

    source_key = '3'
    distances = bellman_ford(graph_obj, graph_obj.get_vertex(source_key))
    for v in distances:
        print('Distance to {}: {}'.format(v.get_key(), distances[v]))
