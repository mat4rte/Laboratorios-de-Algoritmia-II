"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""
#9%
def maior_subCres(num, lista):
    if not lista:
        return 0
    print("NUM: ", num, "num da lista: ", lista[0])
    if num <= lista[0]:
        return 1 + maior_subCres(lista[0], lista[1:])
    else:
        return maior_subCres(num, lista[1:])
    
def crescente(lista):
    
    maior = 0
    
    for pos in range(len(lista)):
        num_sub = maior_subCres(lista[pos], lista[pos:])
        print("num_sub: ",num_sub)
        if num_sub > maior:
            maior = num_sub
    
    return maior
