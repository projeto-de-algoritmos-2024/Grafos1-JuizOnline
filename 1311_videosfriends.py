from collections import deque, defaultdict

# Necessária a criação da classe para que o exercício fosse aceito
class Solution:      
    def watchedVideosByFriends(self, videos_assistidos: dict, amigos: dict, meu_id: int, nivel_desejado: int) -> list[str]:
        """
        Implementação do algortimo BFS para encontrar o menor caminho, porém agora se precisa achar nós em um que estão em um mesmo nível a partir de um nó (usuário com seu ID) inicial
        """

        contagem_videos = defaultdict(int)

        # Já coloca o nó (usuário) inicial na fila e na lista de elementos visitados
        lista_visitados = set([meu_id])
        fila_prox = deque([meu_id])
        amigos_no_nivel = []

        nivel_atual = 0

        while fila_prox:
            if nivel_atual == nivel_desejado:
                amigos_no_nivel.extend(fila_prox)   # A fila fica com os elementos de mesmo nível
                break

            qtd_amigos_nivel = len(fila_prox)
            
            for _ in range(qtd_amigos_nivel):
                noh_u = fila_prox.popleft()

                for amigo_vizinho in amigos[noh_u]:
                    if amigo_vizinho not in lista_visitados:
                        lista_visitados.add(amigo_vizinho)
                        fila_prox.append(amigo_vizinho)

            nivel_atual += 1

        for amigo in amigos_no_nivel:
            for video in videos_assistidos[amigo]:
                contagem_videos[video] += 1

        # Ordena elementos no formato (nome, qtd_vezes) por ordem de quantidade e alfabética
        resultado = sorted(contagem_videos.items(), key=lambda x: (x[1], x[0]))

        return [video for video, _ in resultado]
