from obgraph import Graph

# We first define a graph
graph = Graph.from_dicts(
    node_sequences={
        1: "ACT",
        2: "A",
        3: "G",
        4: "CC"
     },
    edges={
        1: [2, 3],
        2: [4],
        3: [4]
    },
    linear_ref_nodes=[1, 2, 4]  # required, denotes the linear ref path through the graph
)


from graph_kmer_index.kmer_finder import DenseKmerFinder
finder = DenseKmerFinder(graph, k=5)
finder.find()
kmers, nodes = finder.get_found_kmers_and_nodes()

# kmers and nodes are now one kmer and one node for every combination of kmer/node
# e.g. if one kmer touches two nodes, it will be listed twice with the two nodes

print(kmers)
print(nodes)

from graph_kmer_index import kmer_hash_to_sequence
for kmer, node in zip(kmers, nodes):
    print(kmer_hash_to_sequence(kmer, 5), node)
