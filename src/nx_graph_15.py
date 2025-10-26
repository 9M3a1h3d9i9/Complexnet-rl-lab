# networkx graph with 15 nodes

import networkx as nx

def build_nx_graph_15():
    # G = nx.Graph()  # for undirected graph # >> fix the bug
    G = nx.DiGraph()  # for directed graph

    # G.add_edges_from(range(15))  # >> fix the bug
    G.add_nodes_from(range(15)) 

    # Create a 15-node directed graph with realistic capacities.
    # گراف جهت دار با 15 گره و ظرفیت های واقعی ایجاد کنید.
    # Includes forward and small reverse edges for connectivity.
    # شامل یال های رو به جلو و معکوس کوچک برای اتصال است.

    edges =[
        (0,1,10),(0,2,8),(1,3,5),(2,3,6),(1,4,7),(2,5,7),
        (3,6,10),(4,6,6),(5,6,6),(4,7,4),(5,8,4),
        (6,9,12),(7,9,5),(8,9,5),(9,10,10),
        (3,11,3),(11,12,4),(12,13,6),(13,14,8),
        # reverse/alternate edges for realism
        # یال های معکوس/جایگرین برای واقعی گرایی شدن
        (10,7,2),(8,5,2),(5,2,1),(7,4,1)
    ]

    for u,v,c in edges:
        G.add_edge(u, v, capacity=float(c))
        # add small reverse edge if not already present
        # اگر یال معکوسی وجود نداشت، یال معکوس کوچک اضافه کنید
        if not G.has_edge(v, u):
            G.add_edge(v, u, capacity=float(0.5 * c))

    return G

if __name__ == "__main__":
    G = build_nx_graph_15()

    print("Graph created with", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")
    for i, (u, v, d) in enumerate(G.edges(data=True)):
        if i >= 10: break
        print(f"{u} → {v} | capacity = {d['capacity']}")