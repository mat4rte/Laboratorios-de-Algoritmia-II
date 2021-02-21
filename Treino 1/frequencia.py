'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    
    words = {}
    texto = texto.split()
    for palavra in texto:
        num_rep = texto.count(palavra)
        if num_rep not in words:
            words[num_rep] = [palavra]
        else:
            if palavra not in words[num_rep]:
                words[num_rep].append(palavra)
    for rep in words:
        words[rep].sort(reverse = True)
        
  
    
    return [palavra for palavras in words for palavra in words[palavras]][::-1]
