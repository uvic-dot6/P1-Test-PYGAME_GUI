import networkx as nx
import matplotlib.pyplot as plt

class SHOWTREE:
    def __init__(self, tree):
        self.tree = tree

    def transformar_coordenada(self, pos):
        return f"{pos[1] + 1}{chr(pos[0] + 65)}"

    def mostrar_arbol(self):
        G = nx.DiGraph()

        # Agregar nodos y bordes del árbol
        for parent, children in self.tree.items():
            for child in children:
                G.add_edge(self.transformar_coordenada(parent), self.transformar_coordenada(child))

        # Determinar colores de los nodos según el número de hijos
        node_colors = []
        for node in G.nodes():
            parent_pos = (ord(node[1]) - 65, int(node[0]) - 1)
            num_children = len(self.tree.get(parent_pos, []))
            if num_children == 0:
                node_colors.append('lightcoral')  # Color para nodos sin hijos
            elif num_children >= 2:
                node_colors.append('lightblue')  # Color para nodos con 2 o más hijos
            else:
                node_colors.append('lightgreen')  # Color para nodos con 1 hijo

        # Dibujar el grafo con diseño tipo árbol
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")  # Diseño jerárquico
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, font_weight='bold', node_size=700, 
                edge_color="gray", arrows=True, arrowstyle="-|>")

        plt.title("Árbol de Búsqueda DFS Estructurado")
        plt.show()
