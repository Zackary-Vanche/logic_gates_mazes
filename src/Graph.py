class Graph:
    def __init__(self, num_of_nodes=0):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []
        self.node_set = set()

    def add_edge(self, node1, node2, weight):
        self.node_set.add(node1)
        self.node_set.add(node2)
        self.m_num_of_nodes = len(self.node_set)
        self.m_graph.append([node1, node2, weight])
        
    def add_edge_list(self, edge_list):
        for edge in edge_list:
            node1, node2, weight = edge
            self.add_edge(node1, node2, weight)
        
    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])
    
    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1
    
    def kruskals_mst(self):
        # Resulting tree
        mst = []
        
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0
    
        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = {}
        subtree_sizes = {}
    
        # Initialize `parent` and `subtree_sizes` arrays
        for node in self.node_set:
            parent[node] = node
            subtree_sizes[node] = 0
    
        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1
    
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
    
            if x != y:
                e = e + 1
                mst.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        
        # total weight
        total_weight = 0
        for node1, node2, weight in mst:
            total_weight += weight
            
        return {'mst':mst,
                'total_weight':total_weight}