from __future__ import annotations
import os
from collections import defaultdict
import itertools
import json

import networkx as nx
import pandas as pd

def colour_graph(G: nx.Graph, path: str="data") -> nx.Graph:
    with open(os.path.join(path, "character_factions.json")) as f:
        char_facts = json.load(f)
    with open(os.path.join(path, "faction_colours.json")) as f:
        cols = json.load(f)
    nx.set_node_attributes(G, {c: char_facts[c] for c in G.nodes()}, "faction")
    nx.set_node_attributes(G, {c: cols[char_facts[c]] for c in G.nodes()}, "colour")
    return G


def character_graph(name_lists: list[str]) -> nx.Graph:
    """
    Weight is +1 to edge between two characters if they appear in same name list
    """
    edges = defaultdict(lambda: 0)
    for L in name_lists:
        for edge in itertools.combinations(L, r=2): # All pairs of characters
            # Make sure that there is not a difference between (Ned, Sansa) and (Sansa, Ned)
            if edge[0] != edge[1]:
                edge = tuple(sorted(edge))
                edges[edge] += 1
    max_w = len(name_lists)
    G = nx.Graph()
    G.add_weighted_edges_from(((*e, w/max_w) for e, w in edges.items()), weight="weight")

    G = colour_graph(G)
    return G

if __name__ == '__main__':
    datapath = "data"
    localdatapath = "local_data"
    for dataset in ("asoiaf_data_cleaned", "book"):

        df = pd.read_csv(os.path.join(localdatapath, f"{dataset}.csv"), header=0, index_col = 0)
        df["names"] = df.apply(lambda r: eval(r["names"]), axis=1)

        G = character_graph(df["names"])
        print(f"Saving graph for {dataset} to file ...")
        nx.write_gpickle(G, os.path.join(datapath, f"{dataset}.nxgraph"))
