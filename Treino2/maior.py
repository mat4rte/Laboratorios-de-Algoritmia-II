'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def maior(vizinhos):
    
    continentes = {}
    
    for g in vizinhos:
        pertence = 0
        for pais in g:
            if pais not in continentes:              #Entao verificar cada um dos paises que estão no dict, se estiver, adiciono e faço uniao entre g e esse array
                for i in continentes:                
                    if pais in continentes[i]:     
                        pertence = 1
                        continentes[i] = continentes[i].union(g)
                        break;
                
            if not pertence:
                continentes[pais] = set(g)
                break;
    
    maior = 0
    for cont in continentes:
        if len(continentes[cont]) > maior:
            maior = len(continentes[cont])

    return maior
