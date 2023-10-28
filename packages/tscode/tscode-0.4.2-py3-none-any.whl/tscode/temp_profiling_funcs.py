from memory_profiler import profile
from tscode.python_functions import rmsd_and_max
import numpy as np
import networkx as nx

@profile
def prune_conformers_rmsd(structures, atomnos, max_rmsd=0.25, max_delta=None, verbose=False):
    '''
    Removes similar structures by repeatedly grouping them into k
    subgroups and removing similar ones. A cache is present to avoid
    repeating RMSD computations.
    
    Similarity occurs for structures with both RMSD < max_rmsd and
    maximum deviation < max_delta.
    '''

    max_delta = (max_rmsd * 2) if max_delta is None else max_delta

    heavy_atoms = (atomnos != 1)
    heavy_structures = np.array([structure[heavy_atoms] for structure in structures])

    cache_set = set()
    final_mask = np.ones(structures.shape[0], dtype=bool)
    
    for k in (5e5, 2e5, 1e5, 5e4, 2e4, 1e4,
              5000, 2000, 1000, 500, 200, 100,
              50, 20, 10, 5, 2, 1):

        num_active_str = np.count_nonzero(final_mask)
        
        if k == 1 or 5*k < num_active_str:
        # proceed only of there are at least five structures per group

            if verbose:      
                print(f'Working on subgroups with k={k} ({num_active_str} candidates left) {" "*10}', end='\r')

            d = int(len(structures) // k)

            for step in range(int(k)):
            # operating on each of the k subdivisions of the array
                if step == k-1:
                    _l = len(range(d*step, num_active_str))
                else:
                    _l = len(range(d*step, int(d*(step+1))))

                similarity_mat = np.zeros((_l, _l))

                for i_rel in range(_l):
                    for j_rel in range(i_rel+1,_l):

                        i_abs = i_rel+(d*step)
                        j_abs = j_rel+(d*step)

                        if (i_abs, j_abs) not in cache_set:
                        # if we have already performed the comparison,
                        # structures were not similar and we can skip them

                            rmsd, max_dev = rmsd_and_max(heavy_structures[i_abs],
                                                         heavy_structures[j_abs])

                            if rmsd < max_rmsd and max_dev < max_delta:
                                similarity_mat[i_rel,j_rel] = 1
                                break

                for i_rel, j_rel in zip(*np.where(similarity_mat == False)):
                    i_abs = i_rel+(d*step)
                    j_abs = j_rel+(d*step)
                    cache_set.add((i_abs, j_abs))
                    # adding indices of structures that are considered equal,
                    # so as not to repeat computing their RMSD
                    # Their index accounts for their position in the initial
                    # array (absolute index)

                matches = [(i,j) for i,j in zip(*np.where(similarity_mat))]
                g = nx.Graph(matches)

                subgraphs = [g.subgraph(c) for c in nx.connected_components(g)]
                groups = [tuple(graph.nodes) for graph in subgraphs]

                best_of_cluster = [group[0] for group in groups]
                # of each cluster, keep the first structure

                rejects_sets = [set(a) - {b} for a, b in zip(groups, best_of_cluster)]
                rejects = []
                for s in rejects_sets:
                    for i in s:
                        rejects.append(i)

                for i in rejects:
                    abs_index = i + d*step
                    final_mask[abs_index] = 0

    return structures[final_mask], final_mask

@profile
def lowmem_prune_conformers_rmsd(structures, atomnos, max_rmsd=0.25, max_delta=None, verbose=False):
    '''
    Removes similar structures by repeatedly grouping them into k
    subgroups and removing similar ones. A cache is present to avoid
    repeating RMSD computations.
    
    Similarity occurs for structures with both RMSD < max_rmsd and
    maximum deviation < max_delta.
    '''

    max_delta = (max_rmsd * 2) if max_delta is None else max_delta

    heavy_atoms = (atomnos != 1)
    heavy_structures = np.array([structure[heavy_atoms] for structure in structures])

    cache_set = set()
    final_mask = np.ones(structures.shape[0], dtype=bool)
    
    for k in (5e5, 2e5, 1e5, 5e4, 2e4, 1e4,
              5000, 2000, 1000, 500, 200, 100,
              50, 20, 10, 5, 2, 1):

        num_active_str = np.count_nonzero(final_mask)
        
        if k == 1 or 5*k < num_active_str:
        # proceed only of there are at least five structures per group

            if verbose:      
                print(f'Working on subgroups with k={k} ({num_active_str} candidates left) {" "*10}', end='\r')

            d = int(len(structures) // k)

            for step in range(int(k)):
            # operating on each of the k subdivisions of the array
                if step == k-1:
                    _l = len(range(d*step, num_active_str))
                else:
                    _l = len(range(d*step, int(d*(step+1))))

                # similarity_mat = np.zeros((_l, _l))
                matches = set()

                for i_rel in range(_l):
                    for j_rel in range(i_rel+1,_l):

                        i_abs = i_rel+(d*step)
                        j_abs = j_rel+(d*step)

                        if (i_abs, j_abs) not in cache_set:
                        # if we have already performed the comparison,
                        # structures were not similar and we can skip them

                            rmsd, max_dev = rmsd_and_max(heavy_structures[i_abs],
                                                         heavy_structures[j_abs])

                            if rmsd < max_rmsd and max_dev < max_delta:
                                # similarity_mat[i_rel,j_rel] = 1
                                matches.add((i_rel, j_rel))
                                break

                            else:
                                i_abs = i_rel+(d*step)
                                j_abs = j_rel+(d*step)
                                cache_set.add((i_abs, j_abs))
                # for i_rel, j_rel in zip(*np.where(similarity_mat == False)):
                    # i_abs = i_rel+(d*step)
                    # j_abs = j_rel+(d*step)
                    # cache_set.add((i_abs, j_abs))
                    # adding indices of structures that are considered equal,
                    # so as not to repeat computing their RMSD
                    # Their index accounts for their position in the initial
                    # array (absolute index)

                # matches = [(i,j) for i,j in zip(*np.where(similarity_mat))]
                g = nx.Graph(matches)

                subgraphs = [g.subgraph(c) for c in nx.connected_components(g)]
                groups = [tuple(graph.nodes) for graph in subgraphs]

                best_of_cluster = [group[0] for group in groups]
                # of each cluster, keep the first structure

                rejects_sets = [set(a) - {b} for a, b in zip(groups, best_of_cluster)]
                rejects = []
                for s in rejects_sets:
                    for i in s:
                        rejects.append(i)

                for i in rejects:
                    abs_index = i + d*step
                    final_mask[abs_index] = 0

    return structures[final_mask], final_mask
