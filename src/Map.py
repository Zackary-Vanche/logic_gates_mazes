from numpy import ceil as np_ceil

def compute_positions(tree, x=0, y=0, x_step=2, y_step=1):
    """
    Calcule récursivement les positions des nœuds d'un arbre.

    :param tree: Liste représentant l'arbre, e.g., [0, [1, [2, 3], 4]].
    :param x: Position x actuelle du nœud racine.
    :param y: Position y actuelle du nœud racine.
    :param x_step: Espacement horizontal minimal entre les sous-arbres.
    :param y_step: Espacement vertical entre les niveaux de l'arbre.
    :return: Dictionnaire {nœud: (x, y)}.
    """
    # Si le nœud est une feuille (non une liste)
    if not isinstance(tree, list):
        return {tree: (x, y)}

    # Calcul des positions
    positions = {}
    root = tree[0]
    positions[root] = (x, y)

    if len(tree) > 1:
        # Calcul des positions des enfants
        subtree_positions = []
        subtree_widths = []

        for subtree in tree[1:]:
            subtree_pos = compute_positions(subtree, x=0, y=y - y_step, x_step=x_step, y_step=y_step)
            subtree_positions.append(subtree_pos)

            # Calcul de la largeur totale du sous-arbre
            subtree_min_x = min(pos[0] for pos in subtree_pos.values())
            subtree_max_x = max(pos[0] for pos in subtree_pos.values())
            subtree_widths.append(subtree_max_x - subtree_min_x + x_step)

        # Centre des sous-arbres autour du parent
        current_x = x - sum(subtree_widths) / 2

        for i, subtree_pos in enumerate(subtree_positions):
            offset_x = current_x + subtree_widths[i] / 2
            for node, (node_x, node_y) in subtree_pos.items():
                positions[node] = (node_x + offset_x, node_y)
            current_x += subtree_widths[i]

    return positions


def draw_tree_ascii(positions):
    """
    Dessine l'arbre en utilisant des caractères ASCII.

    :param positions: Dictionnaire {nœud: (x, y)}.
    """
    # Normaliser les coordonnées pour l'affichage ASCII
    min_x = min(x for x, y in positions.values())
    max_x = max(x for x, y in positions.values())
    min_y = min(y for x, y in positions.values())

    grid_width = int(np_ceil(max_x - min_x)) + 1
    grid_height = int(np_ceil(abs(min_y))) + 1

    grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

    for node, (x, y) in positions.items():
        grid[int(abs(y))][int(x - min_x)] = str(node)

    # Afficher la grille
    for row in grid:
        print(''.join(row))

def convert_to_tree(graph):
    """
    Convertit une liste de chaînes (représentant un arbre) en une structure d'arbre imbriqué.

    :param graph: Liste de chaînes représentant l'arbre (chaînes de noeuds liés).
    :return: Arbre sous forme de liste imbriquée.
    """
    # Crée un dictionnaire pour stocker les enfants de chaque noeud
    children_map = {}
    for chain in graph:
        parent = chain[0]
        children_map[parent] = chain[1:]  # Stocke tous les enfants sauf le premier (qui est le parent)

    def build_tree(node):
        """
        Fonction récursive pour construire l'arbre imbriqué.
        """
        # Si le noeud n'a pas d'enfants dans le dictionnaire, c'est une feuille
        if node not in children_map or not children_map[node]:
            return [node]
        
        # Sinon, construire une sous-arbre avec ses enfants
        children = [build_tree(child) for child in children_map[node]]
        return [node] + children

    # Construire l'arbre à partir du noeud racine
    root = graph[0][0]  # Supposons que le premier noeud est la racine
    return build_tree(root)


# Exemple d'utilisation
graph = [
    ["A", "B", "C", "D"],
    ["B", "E", "F"],
    ["B", "G", "H"],
    ["C", "I", "J", "K"]
]

tree = [["A",
         ["B",
          ["C", ["D"], ["I", ["J", ["K"]]]],
          ["E", ["F"]],
          ["G", ["H"]]]]]

tree_list = convert_to_tree(graph)

positions = compute_positions(tree_list, x=0, y=0, x_step=4, y_step=2)
draw_tree_ascii(positions) # Je ne comrends pas pourquoi le 12 n'est pas centré en dessous du 9 
