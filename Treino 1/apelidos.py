'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):                   
    lista = {}
    for pessoa in nomes:               
        if len(pessoa.split()) in lista:
            lista[len(pessoa.split())].append(pessoa)
        else:
            lista[len(pessoa.split())] = [pessoa]
               
    for tamanho in lista:
        lista[tamanho].sort()
    return [ pessoa for tam in lista for pessoa in lista[tam]]
    
