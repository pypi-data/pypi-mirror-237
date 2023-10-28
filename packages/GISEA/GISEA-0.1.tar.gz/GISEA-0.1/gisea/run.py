import pandas as pd
import igraph as ig
from time import time
import blitzgsea


def runGISEA(mat, library, processes=6):
    t0 = time()
    print("runGISEA...")

    FullResults = {}

    for i, _ in enumerate(mat.index):
        signature = mat.iloc[i, :].reset_index()
        gene_name = mat.index[i]

        result = blitzgsea.gsea(signature, library, processes=processes)

        FullResults[gene_name] = result.to_dict()
        del result, signature

    print("done in %0.3fs" % (time() - t0))
    return FullResults


def gsea_to_matrix(results, info, obs_dict, pivot=True):
    """
    'es', 'nes', 'pval', 'sidak', 'fdr', 'geneset_size', 'leading_edge', 'leading_edge_size'
    """
    mat = [(obs, term, val) for obs in results for term, val in results[obs][info].items()]
    mat = pd.DataFrame(mat, columns=['Gene', 'Term', info])
    if pivot:
        mat = mat.pivot(index=['Gene'], columns=['Term'], values=info)
    mat.columns.name = None

    mat = mat.loc[obs_dict.keys(),]
    mat.index = obs_dict.values()

    return mat
