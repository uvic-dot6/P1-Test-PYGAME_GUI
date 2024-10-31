import matplotlib.pyplot as plt
import networkx as nx

class SHOWTREE:
    def __init__(self, raiz):
        self.raiz = raiz
     
    def agregar_nodos_al_grafo(self, grafo, nodo, pos, nivel=0, x=0, y=0, ancho=2):
        # Agregar el nodo actual al grafo
        grafo.add_node(nodo.dato)
        pos[nodo.dato] = (x, y)
        
        # Si el nodo tiene hijos, procesarlos
        if nodo.hijos:
            num_hijos = len(nodo.hijos)
            for i, hijo in enumerate(nodo.hijos):
                grafo.add_node(hijo.dato)
                grafo.add_edge(nodo.dato, hijo.dato)
                nuevo_x = x - ancho/2 + (i + 0.5) * ancho/num_hijos
                nuevo_y = y - 1
                self.agregar_nodos_al_grafo(grafo, hijo, pos, nivel + 1, nuevo_x, nuevo_y, ancho/num_hijos)

    def graficar_arbol(self, raiz):
        G = nx.DiGraph()
        pos = {}
        self.agregar_nodos_al_grafo(G, raiz, pos)
        
        plt.figure(figsize=(12, 8))
        
        # Colores para nodos con y sin hijos
        node_colors = ['orange' if G.out_degree(n) == 0 else 'yellow' for n in G.nodes()]
        
        nx.draw(G, pos,
                node_color=node_colors,
                node_size=1500,
                arrows=True,
                arrowsize=10,
                edge_color='black',
                width=2)
        
        labels = {}
        for nodo in G.nodes():
            current = raiz
            stack = [(current, [])]
            while stack:
                current, path = stack.pop(0)
                if current.dato == nodo:
                    labels[nodo] = f'{current.dato}\n costo {current.costo}'
                    break
                for hijo in current.hijos:
                    stack.append((hijo, path + [current]))
        
        nx.draw_networkx_labels(G, pos, labels, font_size=8)
        plt.margins(0.2)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    

class SHOWTREEinformado:
    def __init__(self):
        pass
     
    def agregar_nodos_al_grafo(self, grafo, nodo, pos, nivel=0, x=0, y=0, ancho=2):
        grafo.add_node(nodo.dato)
        pos[nodo.dato] = (x, y)
        
        if nodo.hijos:
            num_hijos = len(nodo.hijos)
            for i, hijo in enumerate(nodo.hijos):
                grafo.add_node(hijo.dato)
                grafo.add_edge(nodo.dato, hijo.dato)
                nuevo_x = x - ancho/2 + (i + 0.5) * ancho/num_hijos
                nuevo_y = y - 1
                self.agregar_nodos_al_grafo(grafo, hijo, pos, nivel + 1, nuevo_x, nuevo_y, ancho/num_hijos)

    def graficar_arbol(self, raiz):
        G = nx.DiGraph()
        pos = {}
        self.agregar_nodos_al_grafo(G, raiz, pos)
        
        plt.figure(figsize=(18, 12))
        
        # Colores para nodos con y sin hijos
        node_colors = ['orange' if G.out_degree(n) == 0 else 'pink' for n in G.nodes()]
        
        nx.draw(G, pos,
                node_color=node_colors,
                node_size=1700,
                arrows=True,
                arrowsize=10,
                edge_color='black',
                width=2)
        
        labels = {}
        for nodo in G.nodes():
            current = raiz
            stack = [(current, [])]
            while stack:
                current, path = stack.pop(0)
                if current.dato == nodo:
                    labels[nodo] = f'{current.dato}\n C: {current.costo} \n D: {current.distancia}\n H:{current.heuristica}'
                    break
                for hijo in current.hijos:
                    stack.append((hijo, path + [current]))
        
        nx.draw_networkx_labels(G, pos, labels, font_size=7)
        plt.margins(0.2)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
