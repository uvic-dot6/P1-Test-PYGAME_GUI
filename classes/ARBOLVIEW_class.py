import matplotlib.pyplot as plt
import networkx as nx

class SHOWTREE:
    def __init__(self, raiz):
        self.raiz = raiz
     
    def agregar_nodos_al_grafo(self,grafo, nodo, pos, nivel=0, x=0, y=0, ancho=2):
        # Agregar el nodo actual al grafo
        grafo.add_node(nodo.dato)
        pos[nodo.dato] = (x, y)
        
        # Si el nodo tiene hijos, procesarlos
        if nodo.hijos:
            num_hijos = len(nodo.hijos)
            for i, hijo in enumerate(nodo.hijos):
                # Agregar el hijo al grafo
                grafo.add_node(hijo.dato)
                # Crear la conexión entre el nodo padre y el hijo
                grafo.add_edge(nodo.dato, hijo.dato)
                # Calcular la posición del hijo
                nuevo_x = x - ancho/2 + (i + 0.5) * ancho/num_hijos
                nuevo_y = y - 1
                # Procesar recursivamente el subárbol del hijo
                self.agregar_nodos_al_grafo(grafo, hijo, pos, nivel + 1, nuevo_x, nuevo_y, ancho/num_hijos)

    def graficar_arbol(self,raiz):
        # Crear un nuevo grafo dirigido
        G = nx.DiGraph()
        
        # Diccionario para almacenar las posiciones de los nodos
        pos = {}
        self.agregar_nodos_al_grafo(G, raiz, pos)
        
        # Crear una nueva figura con un tamaño específico
        plt.figure(figsize=(12, 8))
        
        # Dibujar los nodos y las conexiones
        nx.draw(G, pos,
                node_color='yellow',
                node_size=1500,
                arrows=True,
                arrowsize=10,
                edge_color='black',
                width=2)
        
        # Crear etiquetas personalizadas para cada nodo
        labels = {}
        for nodo in G.nodes():
            # Buscar el nodo correspondiente en el árbol
            current = raiz
            stack = [(current, [])]
            while stack:
                current, path = stack.pop(0)
                if current.dato == nodo:
                    labels[nodo] = f'{current.dato}\n costo {current.costo}'
                    break
                for hijo in current.hijos:
                    stack.append((hijo, path + [current]))
        
        # Dibujar las etiquetas
        nx.draw_networkx_labels(G, pos, labels, font_size=8)
        
        # Ajustar los márgenes y mostrar el gráfico
        plt.margins(0.2)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
