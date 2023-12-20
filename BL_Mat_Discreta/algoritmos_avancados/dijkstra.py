import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        self.distancias = {}

    def add_vertice(self, valor):
        if valor is None:
            raise ValueError("Valor do vértice não pode ser nulo")
        
        self.vertices.add(valor)
        self.arestas[valor] = []

    def add_aresta(self, de_vertice, para_vertice, peso):
        if de_vertice is None or para_vertice is None:
            raise ValueError("Vértices não podem ser nulos")

        if peso is None:
            raise ValueError("Peso da aresta não pode ser nulo")

        self.arestas[de_vertice].append((para_vertice, peso))
        self.arestas[para_vertice].append((de_vertice, peso))

    def dijkstra(self, inicial):
        # Init
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[inicial] = 0
        prioridade = [(0, inicial)]

        while prioridade:
            # vértice com a menor distância
            distancia_atual, vertice_atual = heapq.heappop(prioridade)

            # Verifica vértice repetido
            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.arestas[vertice_atual]:
                nova_distancia = distancia_atual + peso

                # Atualiza a distância se encontrar um caminho mais curto
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(prioridade, (nova_distancia, vizinho))

        return distancias

# vertices
grafo = Grafo()
grafo.add_vertice("X")
grafo.add_vertice("P")
grafo.add_vertice("T")
grafo.add_vertice("O")

grafo.add_aresta("X", "P", 1)
grafo.add_aresta("X", "T", 4)
grafo.add_aresta("P", "T", 2)
grafo.add_aresta("P", "O", 5)
grafo.add_aresta("T", "O", 1)

resultado = grafo.dijkstra("X")
print(resultado)
