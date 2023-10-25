import logging as log
from abc import abstractmethod
from typing import Literal

import networkit as nk
import networkx as nx
import pandas as pd


class Centrality():

    @abstractmethod
    def __init__(self):
        """ Abstract method for "DIY" implementations. """

    @staticmethod
    def degree(G):
        """ Degree centrality. """
        return pd\
            .Series(
                [x[1] for x in G.degree()], name="degree")\
            .astype(float)

    @staticmethod
    def in_degree(G):
        """ In-degree centrality. """
        return pd\
            .Series([x[1] for x in getattr(G, "in_degree", G.degree)],
                    name="in_degree")\
            .astype(float)

    @staticmethod
    def out_degree(G):
        """ Out-degree centrality. """
        return pd\
            .Series([x[1] for x in getattr(G, "out_degree", G.degree)],
                    name="out_degree")\
            .astype(float)

    @staticmethod
    def betweenness_centrality(nkG: nk.Graph, normalized=False):
        """
        Betweenness centrality:
        https://doi.org/10.1080/0022250X.2001.9990249
        """
        bet = nk.centrality.Betweenness(nkG, normalized)

        return pd.Series(
            bet.run().scores(),
            name="betweenness_centrality"
        )

    @staticmethod
    def betweenness_approx(nkG: nk.Graph, epsilon=0.01, delta=0.1, universal_constant=1.0):
        """
        Approximate betweenness centrality:
        https://doi.org/10.1145/2556195.2556224
        """
        bet = nk.centrality.ApproxBetweenness(
            nkG,
            epsilon,
            delta,
            universal_constant
        )

        return pd.Series(
            bet.run().scores(),
            name="betweenness_approx"
        )

    @staticmethod
    def betweenness_est(nkG: nk.Graph, n_samples=100, normalized=False, parallel_flag=False):
        """
        Estimated betweenness centrality:
        http://doi.org/10.1137/1.9781611972887.9
        """
        bet = nk.centrality.EstimateBetweenness(
            nkG,
            n_samples,
            normalized,
            parallel_flag
        )

        return pd.Series(
            bet.run().scores(),
            name="betweenness_est"
        )

    @staticmethod
    def betweenness_kadabra(nkG: nk.Graph, err=0.05, delta=0.8, deterministic=False, k=0):
        """
        Kadabra betweenness centrality:
        https://arxiv.org/abs/1903.09422
        """
        bet = nk.centrality.KadabraBetweenness(
            nkG,
            err,
            delta,
            deterministic,
            k
        )

        return pd.Series(
            bet.run().scores(),
            name="betwenness_kadabra"
        )

    @staticmethod
    def bridging_centrality(G: nx.Graph, betweenness={}, bridging_coef={}):
        """
        Bridging centrality:
        https://cse.buffalo.edu/tech-reports/2006-05.pdf
        """
        if not betweenness:
            betweenness = nx.betweenness_centrality(G)

        if not bridging_coef:
            bridging_coef = Centrality.bridging_coef(G)
            bridging_coef.index = G.nodes()

        return pd.Series(
            [betweenness[node] * bridging_coef[node] for node in G.nodes()],
            name="bridging_centrality"
        )

    @staticmethod
    def bridging_coef(G: nx.Graph, degree={}):
        """
        Bridging coefficient:
        https://cse.buffalo.edu/tech-reports/2006-05.pdf
        """
        bc = {}

        if not degree:
            degree = nx.degree_centrality(G)

        for node in G.nodes():
            bc[node] = 0

            if degree[node] > 0:
                neighbors_degree = dict(
                    nx.degree(G, nx.neighbors(G, node))).values()

                sum_neigh_inv_deg = sum(
                    (1.0/d) for d in neighbors_degree)

                if sum_neigh_inv_deg > 0:
                    bc[node] = (1.0/degree[node]) / sum_neigh_inv_deg

        return pd.Series(
            bc.values(),
            name="bridging_coef"
        )

    @staticmethod
    def brokering_centrality(G: nx.Graph, degree={}, clustering={}):
        """
        Brokering centrality:
        https://doi.org/10.1093/gbe/evq064
        """
        if not degree:
            degree = nx.degree_centrality(G)

        if not clustering:
            clustering = nx.clustering(G)

        return pd.Series(
            [(1 - clustering[node]) * degree[node] for node in G.nodes()],
            name="brokering_centrality"
        )

    @staticmethod
    def closeness_centrality(nkG: nk.Graph, normalized=True, variant: Literal["generalized", "standard"] = "generalized"):
        """
        Closeness centrality:
        https://www.theses.fr/2015USPCD010.pdf
        """
        if variant == "generalized":
            variant = nk.centrality.ClosenessVariant.Generalized
        elif variant == "standard":
            variant = nk.centrality.ClosenessVariant.Standard
        else:
            raise ValueError(
                f"Invalid closeness variant (variant='{variant}').\n\n"
                f"Available choices: 'standard' or 'generalized' (default)."
            )

        closeness = nk.centrality.Closeness(
            nkG,
            normalized,
            variant
        )

        return pd.Series(
            closeness.run().scores(),
            name="closeness_centrality"
        )

    @staticmethod
    def closeness_approx(nkG: nk.Graph, n_samples=100, normalized=True):
        """
        Approximate closeness centrality:
        https://doi.org/10.1145/2660460.2660465
        """
        closeness = nk.centrality.ApproxCloseness(
            nkG,
            n_samples,
            normalized
        )

        return pd.Series(
            closeness.run().scores(),
            name="closeness_approx"
        )

    @staticmethod
    def clustering_centrality(nkG: nk.Graph, remove_self_loops=True, to_undirected=True, turbo=False):
        """
        Local clustering coefficient:
        https://doi.org/10.1137/1.9781611973198.1

        Turbo mode aimed at graphs with skewed, high degree distribution:
        https://dl.acm.org/citation.cfm?id=2790175
        """
        nkGu = nk.graphtools.toUndirected(nkG) if to_undirected else nkG
        nkGu.removeSelfLoops() if remove_self_loops else None

        clustering = nk.centrality.LocalClusteringCoefficient(
            nkGu,
            turbo=turbo
        )

        return pd.Series(
            clustering.run().scores(),
            name="clustering"
        )

    @staticmethod
    def eigenvector_centrality(nkG: nk.Graph):
        """
        Implementierung der Eigenvektor-Zentralität:
        https://doi.org/10.1007%2FBF01449896
        """
        eig = nk.centrality.EigenvectorCentrality(nkG)

        return pd.Series(
            eig.run().scores(),
            name="eigenvector"
        )

    @staticmethod
    def page_rank(nkG: nk.Graph, cc: Literal["l1", "l2"] = "l2", max_iterations=None):
        """
        PageRank, a variant of eigenvector centrality:
        http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf
        """
        pr = nk.centrality.PageRank(nkG)

        if max_iterations:
            pr.maxIterations = max_iterations

        if cc == "l1":
            pr.norm = nk.centrality.Norm.l1norm

        elif cc != "l2":
            raise ValueError(
                f"Invalid convergence criterion (cc='{cc}').\n\n"
                f"Available choices: 'l1' or 'l2' (default)."
            )

        return pd.Series(
            pr.run().scores(),
            name="page_rank"
        )

    @staticmethod
    def katz_centrality(nkG: nk.Graph):
        """
        Katz centrality:
        https://doi.org/10.1007/BF02289026
        """
        katz = nk.centrality.KatzCentrality(nkG)

        return pd.Series(
            katz.run().scores(),
            name="katz_centrality"
        )

    @staticmethod
    def laplacian_centrality(nkG: nk.Graph):
        """
        Laplacian centrality:
        https://doi.org/10.1016/j.ins.2011.12.027
        """
        laplacian = nk.centrality.LaplacianCentrality(nkG)

        return pd.Series(
            laplacian.run().scores(),
            name="laplacian_centrality"
        )

    @staticmethod
    def weighted_degree(G, weight="weight"):
        """ Weighted degree centrality. """
        N = list(G.nodes())
        E = nx.to_pandas_edgelist(G)

        if not G.is_directed():
            return Centrality.degree(G)

        if G.is_directed() and weight not in E.columns:
            raise IndexError(f"Edge weight attribute '{weight}' not found. Available attributes: {list(E.columns)}.")

        Ws = E[["source", weight]].groupby(["source"]).sum(weight)
        Wt = E[["target", weight]].groupby(["target"]).sum(weight)

        W = Ws.add(Wt, fill_value=0).squeeze("columns")
        W.name = "weighted_degree"
        W.index = [N.index(n) for n in W.index]
        W.index.name = None
        return W.astype(float)

    @staticmethod
    def weighted_in_degree(G, weight="weight"):
        """ Weighted in-degree centrality. """
        N = list(G.nodes())
        E = nx.to_pandas_edgelist(G)

        if not G.is_directed():
            return Centrality.in_degree(G)

        if G.is_directed() and weight not in E.columns:
            raise IndexError(f"Edge weight attribute '{weight}' not found. Available attributes: {list(E.columns)}.")

        W = E[["source", weight]].groupby(["source"]).sum(weight).squeeze("columns")
        W.name = "weighted_in_degree"
        W.index = [N.index(n) for n in W.index]
        W.index.name = None
        return W.astype(float)

    @staticmethod
    def weighted_out_degree(G, weight="weight"):
        """ Weighted out-degree centrality. """
        N = list(G.nodes())
        E = nx.to_pandas_edgelist(G)

        if not G.is_directed():
            return Centrality.out_degree(G)

        if G.is_directed() and weight not in E.columns:
            raise IndexError(f"Edge weight attribute '{weight}' not found. Available attributes: {list(E.columns)}.")

        W = E[["target", weight]].groupby(["target"]).sum(weight).squeeze("columns")
        W.name = "weighted_out_degree"
        W.index = [N.index(n) for n in W.index]
        W.index.name = None
        return W.astype(float)
