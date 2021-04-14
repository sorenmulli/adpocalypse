import os
from collections import defaultdict
import itertools

import networkx as nx
import pandas as pd

def character_graph(name_lists: list[str]):
    """
    Weight is +1 to edge between two characters if they appear in same name list
    """
    edges = defaultdict(0)
    for L in name_lists:
        for edge in itertools.combinations(L):
            # Make sure that there is not a difference between (Ned, Sansa) and (Sansa, Ned)
            edge = tuple(sorted(edge))
            edges[edge] += 1
    G = nx.Graph()
    G.add_weighted_edges_from(((*e, w) for e, w in edges.items()), weight="weight")


if __name__ == '__main__':
    datapath = "local_data"

    df = pd.read_csv(os.path.join(datapath, "chapters.csv"), header=0, index_col=0)
    df["names"] = df.apply(lambda r: eval(r["names"]), 1)
