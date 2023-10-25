import logging as log
from inspect import signature
from typing import Optional

import networkx as nx
import pandas as pd

from .base import (
    Centrality,
    Convert,
    Graph,
    Layout,
    Partition,
    Plot,
    # Subgraph,
    DEFAULT_LAYOUT
)

log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log.basicConfig(format=log_format, level=log.INFO)

DEFAULT_ATTRS = [
    "degree", "in_degree", "out_degree",
    "weighted_degree", "weighted_in_degree", "weighted_out_degree"]


class GraphExpress(Graph, Centrality, Convert, Layout, Partition, Plot):

    @staticmethod
    def compute(G: nx.Graph,
                attrs: Optional[list] = DEFAULT_ATTRS,
                fillna: Optional[None] = 0,
                normalize: bool = False,
                **kwargs) -> pd.DataFrame:
        """
        Returns centralities and partitions in a single data frame indexed by node label.
        """
        method_class = GraphExpress._method_class((Centrality, Partition))
        method_input = GraphExpress._method_input(globals(), method_class)

        if not G.order():
            raise RuntimeError(
                f"Graph is empty (nodes: {G.order()}, edges: {G.size()}")

        df = pd.DataFrame()
        attrs = [attrs] if type(attrs) == str else attrs

        for attr in attrs:
            if attr not in method_class:
                raise RuntimeError(
                    f"Invalid node attribute ('{attr}'). " +
                    f"Available choices: {list(method_class.keys())}.")

        nkG = None
        if any(method_input[attr] == "nkG" for attr in attrs):
            log.debug("Converting NetworkX graph to Networkit format...")
            nkG = Convert.nx2nk(G)

        iG = None
        if any(method_input[attr] == "iG" for attr in attrs):
            log.debug("Converting NetworkX graph to igraph format...")
            iG = Convert.nx2ig(G)

        for attr in attrs:
            log.info(f"Computing '{attr}' attribute...")
            # Get method to compute attribute.
            method = getattr(globals()[method_class[attr]], attr)
            # Get graph required by function (NetworkX, Networkit, or Igraph).
            graph = locals()[method_input[attr]]
            # Get parameters either from dictionary indexed by attribute key or from keyword arguments.
            params = kwargs.get(attr, {arg: kwargs[arg] for arg in signature(method).parameters if arg in kwargs})
            # Compute and index as a new data frame column with attribute name.
            df[attr] = method(graph, **params) if G.order() else ()

        if normalize:
            # All attributes, except partitions (dtype=int).
            columns = df.select_dtypes(float).columns
            df[columns] = df[columns].apply(lambda x: x / x.max())

        df.index = G.nodes()
        df.index.name = "id"

        return df.fillna(fillna)

    @staticmethod
    def describe(G: nx.Graph) -> pd.DataFrame:
        """
        Quickly describes graph stucture.
        """
        print(
            f"Graph ({'directed' if G.is_directed() else 'undirected'}) "
            f"has {G.order()} nodes and {G.size()} edges (density: {GraphExpress.density(G, True)})."
        )

    @staticmethod
    def _method_class(classes: list) -> dict:
        """
        Returns dictionary of methods and classes.
        """
        return {
            method: Class.__name__
            for Class in classes
            for method in dir(Class)
            if not method.startswith("__")
        }

    @staticmethod
    def _method_input(globals: dict, method_class: dict) -> dict:
        """
        Returns dictionary of methods and input graph object
        type (G: NetworkX, nkG: Networkit, iG: igraph).
        """
        return {
            m: list(signature(getattr(globals[c], m)).parameters.keys())[0]
            for m, c in method_class.items()
        }
