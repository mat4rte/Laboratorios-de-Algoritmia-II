'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def area(p, mapa):
    
    visitou = []
    x,y = p
    p = (y,x)
    if 0 <= x < len(mapa) and 0 <= y < len(mapa[x]):
        visitou = areaAux(p, mapa, [])
        
    return len(visitou)


def areaAux(p, mapa, visitados):
    
    x,y = p
    if x + 1 < len(mapa) and mapa[x + 1][y] == '.' and (x + 1, x) not in visitados:   #baixo
        if p not in visitados:
            visitados.append(p)
        p = (x + 1,y)
        areaAux(p, mapa, visitados)
    if x - 1 >= 0 and mapa[x - 1][y] == '.' and (x - 1, y) not in visitados:     #cima
        if p not in visitados:
            visitados.append(p)
        p = (x - 1,y)
        areaAux(p, mapa, visitados)
    if y + 1 < len(mapa) and mapa[x][y + 1] == '.' and (x, y + 1) not in visitados:     #dir
        if p not in visitados:
            visitados.append(p)
        p = (x,y + 1)
        #visitados.append(p)
        areaAux(p, mapa, visitados)
    if y - 1 >= 0 and mapa[x][y - 1] == '.' and (x, y - 1) not in visitados:     #esq
        if p not in visitados:
            visitados.append(p)
        p = (x,y - 1)
        #visitados.append(p)
        areaAux(p, mapa, visitados)
    elif p not in visitados:
        visitados.append(p)
    
    
    return visitados
