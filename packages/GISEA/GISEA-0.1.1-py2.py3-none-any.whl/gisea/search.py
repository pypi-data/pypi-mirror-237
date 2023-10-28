import pandas as pd
import igraph as ig
import networkx as nx


def node_i(graph, node):
    return [i for i, x in enumerate(graph.vs['name']) if x == node][0]


def run_bfs(graph, node, distance=1):
    """Run BFS – Breadth-First Traversal (or Search)
    This function is running BFS algorithm to create a subgraph for given 1) `igraph` object, 2) node id, and 3) distance from the node.
    The subgraph includes all nodes with certain distance (defualt 1) from the given node.
    """
    A = [edge.tuple for edge in graph.es]
    G = nx.Graph(A)
    bfs = nx.descendants_at_distance(G, source=node_i(graph, node), distance=distance)
    out = [graph.vs['name'][i] for i in list(bfs)]
    return out


def nodes2df(G):
    node_df = pd.DataFrame({attr: G.vs[attr] for attr in G.vertex_attributes()})
    return node_df


def get_graph_features(g):
    print(g.summary(), '\n')
    print("Number of vertices in the graph:", g.vcount())
    print("Number of edges in the graph", g.ecount())
    print("Is the graph directed:", g.is_directed())
    print("Maximum degree in the graph:", g.maxdegree())

    top_nodes = g.vs.select(_degree=g.maxdegree())["name"]
    print("Node name with Maximum degree:", top_nodes)


def filter_graph_by_weight(G, weight_thr, side, verbose=True):
    """subset graph by weight threshold
    """
    keep = None

    if side == 'above':
        keep = [i for i, x in enumerate(G.es['weight']) if x >= weight_thr]
    elif side == 'below':
        keep = [i for i, x in enumerate(G.es['weight']) if x <= weight_thr]
    elif side == 'both':
        keep = [i for i, x in enumerate(G.es['weight']) if abs(x) >= weight_thr]

    outG = G.es.select(keep).subgraph()

    if verbose: get_graph_features(outG)

    return outG


def filter_graph_by_geneset(G, geneset, max_distance=1, verbose=True):
    """filter GI map by running BFS for given gene sets
    """
    bfs = []
    for gene in geneset:
        for distance in range(1, max_distance + 1):
            bfs = bfs + run_bfs(G, gene, distance=distance)
    
    outG = G.vs.select(name_in=bfs + geneset).subgraph()
    
    if verbose: get_graph_features(outG)
    
    return outG


def filter_graph_by_targets(inG, targets, max_distance=2, weight_thr=None, verbose=True):
    """filter given graph by running BFS for given targets
    """
    # filter adjacencies by given target genes 
    if type(targets) is str:
        targets = [targets]

    bfs = []
    for gene in targets:
        for distance in range(1, max_distance + 1):
            bfs = bfs + run_bfs(inG, gene, distance=distance)

    outG = inG.vs.select(name_in=bfs + targets).subgraph()

    # subset graph by weight threshold 
    if weight_thr:
        outG = outG.es.select([i for i, x in enumerate(outG.es['weight']) if x >= weight_thr]).subgraph()
    if verbose: get_graph_features(outG)

    return outG


def plot_graph(G, layout="kk", main_node=None, target=None, b1=350, b2=350):
    """visualising graph data

    - Creating a graph
    - Visualising the graph
    - Obtaining information on the vertices and edges of the graph
    - Obtaining adjacent vertices to a vertex
    - Breadth-first search (BFS) from a vertex
    - Determining shortest paths from a vertex
    - Obtain the Laplacian matrix of a graph
    - Determine the maximum flow between the source and target vertices
    """
    # G.vs["color"] = [
    #     "lightblue" if (vertex['name'] in [x.replace('(+)', '') for x in auc_mtx.columns.to_list()])
    #     else "lightgray" for vertex in G.vs
    # ]

    if main_node in G.vs['name']:
        G.vs[[i for i, x in enumerate(G.vs['name']) if x == main_node][0]]['color'] = 'yellow'

    return ig.plot(
        G,
        layout=G.layout(layout),
        vertex_label=G.vs["name"],
        vertex_color=G.vs["color"],
        vertex_label_size=6, vertex_size=35,
        bbox=(b1, b2), margin=20,
        #         target=target
    )
