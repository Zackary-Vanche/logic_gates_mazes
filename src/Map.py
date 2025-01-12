from numpy import ceil as np_ceil
from numpy import log

# def make_chain(l):
#     chain = [l.pop()]
#     l.reverse()
#     for x in l:
#         if isinstance(x, list):
#             pass
#         else:
#             chain = [x, chain]
#     return chain

def make_chain(*args):
    # Si des arguments sont passés en tant que liste, les traiter comme une liste
    if len(args) == 1 and isinstance(args[0], list):
        l = args[0]
    else:
        # Sinon, on les traite comme une liste d'éléments individuels
        l = list(args)
    assert len(l) != 0
    if len(l) == 1:
        assert not isinstance(l[0], list)
        return l
    chain = [l[0]]
    for i in range(1, len(l)):
        if isinstance(l[i], list):
            chain.append(l[i])
        else:
            chain.append(make_chain(l[i:]))
            break
    return chain
        
def make_positions_dict(tree, tree_positions):
    positions_dict = {tree[0]:tree_positions[0]}
    for i in range(1, len(tree)):
        positions_dict = positions_dict|make_positions_dict(tree[i], tree_positions[i])
    return positions_dict

def make_nodes_dict(tree, prefix=''):
    try:
        if isinstance(tree, list):
            nodes_dict = {prefix:tree[0]}
            for i in range(1, len(tree)):
                nodes_dict = nodes_dict|make_nodes_dict(tree[i], prefix=prefix+f'_{str(i)}')
        else:
            nodes_dict = {prefix:tree}
        return nodes_dict
    except:
        print('*'*50)
        print(tree)
        print('*'*50)
        raise
        
def make_children_dict(tree, prefix=''):
    if isinstance(tree, list):
        children_names = []
        for i in range(1, len(tree)):
            children_names.append(prefix+f'_{str(i)}')
        children_dict = {prefix:children_names}
        for i in range(1, len(tree)):
            children_dict = children_dict|make_children_dict(tree[i], prefix=prefix+f'_{str(i)}')
    else:
        children_dict = {prefix:[]}
    return children_dict

def make_edges_list(tree):
    edges_list = []
    root = tree[0]
    for i in range(1, len(tree)):
        subtree = tree[i]
        edges_list.append([root, subtree[0]])
        edges_list.extend(make_edges_list(subtree))
    return edges_list 
    
def draw_tree_ascii(tree, tree_positions):
    """
    Dessine l'arbre en utilisant des caractères ASCII.

    :param positions: Dictionnaire {nœud: (x, y)}.
    """
    positions = make_positions_dict(tree, tree_positions)
    
    # Normaliser les coordonnées pour l'affichage ASCII
    min_x = min(x for x, y in positions.values())
    max_x = max(x for x, y in positions.values())
    min_y = min(y for x, y in positions.values())
    max_y = max(y for x, y in positions.values())
    
    nx = 4
    ny = 2
    
    grid_width = int(np_ceil(max_x - min_x)) + 1
    grid_height = int(np_ceil(max_y - min_y)) + 1

    grid = [[' ' for _ in range(nx*grid_width)] for _ in range(ny*grid_height)]

    for node, (x, y) in positions.items():
        grid[ny*int(abs(y))][nx*int(x - min_x)] = str(node)

    # Afficher la grille
    for row in grid:
        print(''.join(row))
        
def translate_tree_position(tree_list, dx, dy):
    root_x, root_y = tree_list[0]
    translated_tree_list = [(root_x+dx, root_y+dy)]
    for child in tree_list[1:]:
        translated_tree_list.append(translate_tree_position(child, dx, dy))
    return translated_tree_list

def get_bounding_box(tree_list):
    root_x, root_y = tree_list[0]
    min_x, max_x, min_y, max_y = root_x, root_x, root_y, root_y
    for child in tree_list[1:]:
        min_x_child, max_x_child, min_y_child, max_y_child = get_bounding_box(child)
        min_x = min(min_x, min_x_child)
        max_x = max(max_x, max_x_child)
        min_y = min(min_y, min_y_child)
        max_y = max(max_y, max_y_child)
    return min_x, max_x, min_y, max_y

def translate_to_0(tree_list):
    min_x, max_x, min_y, max_y = get_bounding_box(tree_list)
    return translate_tree_position(tree_list, min_x, 0)

def orientation(p, q, r):
    """Retourne l'orientation des points p, q, r.
    0 -> colinéaires
    1 -> horaire
    2 -> antihoraire
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def on_segment(p, q, r):
    """Vérifie si le point q est sur le segment pr"""
    if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
        return True
    return False

def segments_intersect(s1, s2):
    """Retourne True si les segments s1 et s2 s'intersectent."""
    p1, p2 = s1
    p3, p4 = s2

    # Calcul des orientations pour les paires de points
    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    # Cas généraux : les orientations doivent être opposées pour chaque segment
    if o1 != o2 and o3 != o4:
        return True

    # Cas particuliers : les segments sont colinéaires et se superposent
    if o1 == 0 and on_segment(p1, p3, p2):
        return True
    if o2 == 0 and on_segment(p1, p4, p2):
        return True
    if o3 == 0 and on_segment(p3, p1, p4):
        return True
    if o4 == 0 and on_segment(p3, p2, p4):
        return True

    return False

def intersect_tree(tp0, tp1, e):
    try:
        nodes_0 = make_nodes_dict(tp0).values()
        nodes_1 = make_nodes_dict(tp1).values()
        for p in nodes_0:
            for q in nodes_1:
                if ((p[0]-q[0])**2+(p[1]-q[1])**2)**(1/2) < e:
                    return True
        edges_0 = make_edges_list(tp0)
        edges_1 = make_edges_list(tp1)
        for e0 in edges_0:
            for e1 in edges_1:
                if segments_intersect(e0, e1):
                    # print(e0, e1)
                    return True
        return False
    except:
        print(tp0, tp1, nodes_0, nodes_1, edges_0, edges_1)
        raise
        
def compute_positions(tree_list, y=0):
    if not isinstance(tree_list, list):
        return [[0, y]]
    if len(tree_list) == 1:
        return [[0, y]]
    children_positions = []
    children_root_positions = []
    children = tree_list[1:]
    dx = 0
    
    xmax = -float('inf')
    xmin = float('inf')
    for child in children:
        child_position = compute_positions(child, y+1)
        child_position = translate_tree_position(child_position, dx, 0)
        min_x_child, max_x_child, min_y_child, max_y_child = get_bounding_box(child_position)
        xmax = max(xmax, child_position[0][0])
        xmin = min(xmin, child_position[0][0])
        dx += max_x_child - min_x_child + 1
        children_positions.append(child_position)
        children_root_positions.append(child_position[0])
        
    # last_child_position = None
    # xmax = -float('inf')
    # xmin = float('inf')
    # for child in children:
    #     child_position = compute_positions(child, y+1)
    #     if not last_child_position is None:
    #         dx = 1
    #         e = 2
    #         while intersect_tree(last_child_position, child_position, e):
    #             child_position = translate_tree_position(child_position, dx, 0)
    #     children_positions.append(child_position)
    #     children_root_positions.append(child_position[0])
    #     min_x_child, max_x_child, min_y_child, max_y_child = get_bounding_box(child_position)
    #     xmax = max(xmax, child_position[0][0])
    #     xmin = min(xmin, child_position[0][0])
    #     last_child_position = child_position
    
    x = sum([p[0] for p in children_root_positions])/len(children_root_positions)
    dy = log(xmax-xmin+1)*0.5
    children_positions = [translate_tree_position(child_position, 0, dy) for child_position in children_positions]
    tree_positions = translate_to_0([(x, y)] + children_positions)
    return tree_positions
    
if __name__ == "__main__":
    tree = ["A",
             ["B",
              make_chain(["C", "D", "E"]),
              make_chain(["F", "G", "H"]),
              make_chain(["I", "J", "K", make_chain(["L", "M", "N"]), "O"]),
              make_chain(["P", "Q", "R", make_chain(["S", "T"]), make_chain(["U", "V"])]),
              ['W', 'X', 'Y', 'Z']]
             ]
    
    print(tree)
    
    positions = compute_positions(tree, y=0)
    draw_tree_ascii(tree, positions)

class Map:
    
    pass