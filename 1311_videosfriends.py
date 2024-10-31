from collections import deque, defaultdict


def watchedVideosByFriends(videos_assistidos: dict, amigos: dict, meu_id: int = 0, nivel_desejado: int = 0) -> list[str]:
    contagem_videos = defaultdict(int)

    amigos_no_nivel = bfs_amigos(amigos, meu_id, nivel_desejado)    # Descobre quantos usuários tem em tal nível do grafo, utilizando BFS

    for amigo in amigos_no_nivel:
        for video in videos_assistidos[amigo]:
            contagem_videos[video] += 1

    # Ordena os resultados em ordem alfabética e por quantidade, retornando apenas os nome dos filmes
    resultado = sorted(contagem_videos.items(), key=lambda x: (x[1], x[0]))

    return [video for video, _ in resultado]

def bfs_amigos(grafo : dict, node_start: int, nivel_desejado: int):
    lista_visitados = set([node_start])
    fila_prox = deque([node_start])
    filmes_vistos = []

    nivel_atual = 0

    # Aplica o algoritmo de BFS, porém para a busca quando se chega ao nível desejado
    while fila_prox:
        if nivel_atual == nivel_desejado:
            filmes_vistos.extend(fila_prox)
            break

        qtd_cidades_nivel = len(fila_prox)
        
        for _ in range(qtd_cidades_nivel):
            noh_u = fila_prox.popleft()

            for noh_vizinho in grafo[noh_u]:
                if noh_vizinho not in lista_visitados:
                    lista_visitados.add(noh_vizinho)
                    fila_prox.append(noh_vizinho)

        nivel_atual += 1
    
    return filmes_vistos