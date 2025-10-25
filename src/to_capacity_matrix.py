import numpy as np
from src.nx_graph_15 import build_nx_graph_15

def nx_to_capacity_matrix(G):
    # Convert a NetworkX DGraph with 'capacity' attributes to
    # a NumPy capacity matrix.
    n = G.number_of_nodes()
    cap = np.zeros((n, n), dtype=float)
    
    # Output :
    #     cap[u][v] = capacity of edge u->v, 0 if no edge.
    for u, v, d in G.edges(data=True):
        cap[u][v] = d.get('capacity', 0.0) 
        # aggregate if multiple edges exist
    return cap

if __name__ == "__main__":
    G = build_nx_graph_15()
    cap_matrix = nx_to_capacity_matrix(G)
    
    # print("Capacity Matrix:")
    # print(cap_matrix)

    C = nx_to_capacity_matrix(G)
    print("Capacity matrix shape:", C.shape)
    
    nz = np.argwhere(C > 0)
    print("Non-zero entries:", len(nz))
    
    for i, (u, v) in enumerate(nz[ :10]):
        print(f" C[{u}, {v}] = {C[u, v]:.2f}")
