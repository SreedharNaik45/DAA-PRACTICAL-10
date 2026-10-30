V = 5
edges = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D'),
    (6, 'C', 'E'),
    (2, 'D', 'E')
]
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True
def kruskal(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    edges.sort()
    mst = []
    total_cost = 0
    for weight, u, v in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight
        if len(mst) == len(vertices) - 1:
            break
    if len(mst) != len(vertices) - 1:
        print("Graph is disconnected.")
        return
    print("Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)
    print("Total Minimum Cost:", total_cost)
vertices = ['A', 'B', 'C', 'D', 'E']
kruskal(vertices, edges)
