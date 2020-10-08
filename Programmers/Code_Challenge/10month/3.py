import math

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

def bellmanFord(graph, s):
    d = dict.fromkeys(graph.V, math.inf)
    pi = dict.fromkeys(graph.V, None)

    d[s] = 0

    def relax(u, v, w):
        if d[v] > d[u] + w:
            d[v] = d[u] + w
            pi[v] = u

    for i in graph.V[:-1]:
        for u, v, w in graph.edges:
            relax(u, v, w)

    return d, pi

def solution(n, edges):
    answer = 0

    v = [i+1 for i in range(n)]
    g = Graph(v)

    for e in edges:
        g.add_edge(e+[1])
        g.add_edge(e[::-1]+[1])

    root = v[0]
    d, _ = bellmanFord(g, root)

    v1 = sorted(d.items(), key = lambda x:x[1])[-1][0]
    d1, _ = bellmanFord(g, v1)
    d1_sort = sorted(d1.items(), key = lambda x:x[1])

    v2 = d1_sort[-1][0]
    d2, _ = bellmanFord(g, v2)
    d2_sort = sorted(d2.items(), key = lambda x:x[1])

    answer = max(answer, d1_sort[-2][1])
    answer = max(answer, d2_sort[-2][1])
        
    return answer

n = 4
n = 5
edges = [[1,2],[2,3],[3,4]]
edges = [[1,5],[2,5],[3,5],[4,5]]
print(solution(n, edges))
