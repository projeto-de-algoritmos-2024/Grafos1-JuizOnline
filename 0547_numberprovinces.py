class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        Função que irá retornar as províncias (componentes conectados) das cidades, onde 'isConnected' é a matriz de adjacência das cidades
        """

        num_provincias = 0
        cidades_visitadas = []

        # A cada saída do método de visitar uma cidade, se sabe que não existem outros vizinhos, gerando um componente conectado (província)
        for cidade in range(0, len(isConnected)):
            if cidade not in cidades_visitadas:
                self.cidadeVisitada(cidade, isConnected, cidades_visitadas)
                num_provincias += 1

        return num_provincias

    # Por se tratar de uma matriz de adjacência ao invés de uma lista, a lógica muda um pouquinho
    def cidadeVisitada(self, cidade, isConnected, visitados) -> None:
        visitados.append(cidade)

        for vizinho in range(0, len(isConnected[cidade])):
            if isConnected[cidade][vizinho] and vizinho != cidade and vizinho not in visitados:
                self.cidadeVisitada(vizinho, isConnected, visitados)