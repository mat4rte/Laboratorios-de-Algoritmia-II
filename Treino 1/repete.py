'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    
    seq = palavra
    iguais = ""
    for i in range(len(palavra)):
        if palavra[i] == palavra[len(palavra) - i - 1]:
            iguais+=palavra[i]
            seq = seq[:-1]
        else:
            break
    
    return seq*n+iguais
