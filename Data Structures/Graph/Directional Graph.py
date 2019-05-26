"""
Graph and its representations
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not same as
(v, u) in case of a directed graph(di-graph). The pair of the form (u, v) indicates that there is an edge from vertex u
to vertex v. The edges may contain weight/value/cost.

Graphs are used to represent many real-life applications: Graphs are used to represent networks. The networks may
include paths in a city or telephone network or circuit network. Graphs are also used in social networks like linkedIn,
Facebook. For example, in Facebook, each person is represented with a vertex(or node). Each node is a structure and
contains information like person id, name, gender and locale. See this for more applications of graph.

GFG: https://www.geeksforgeeks.org/graph-and-its-representations/
"""


class Vertex:
    def __init__(self, value):
        self.name = value
        self.neighbors = {}

    def add_neighbors(self, v):
        self.neighbors[v] = self.name


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and not self.vertices.get(vertex.name):
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, source_vertex, destination_vertex):
        if self.vertices.get(source_vertex) and self.vertices.get(destination_vertex):
            self.vertices[source_vertex].add_neighbors(destination_vertex)
            return True
        else:
            return False

    def print_graph(self):
        for vertex, edge in self.vertices.items():
            print('Vertex -> ', vertex)
            print('Neighbours:', edge.neighbors)


if __name__ == '__main__':
    graph = Graph()

    a = Vertex('A')
    graph.add_vertex(a)

    b = Vertex('B')
    graph.add_vertex(b)

    c = Vertex('C')
    graph.add_vertex(c)

    d = Vertex('D')
    graph.add_vertex(d)

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'A')

    graph.print_graph()
