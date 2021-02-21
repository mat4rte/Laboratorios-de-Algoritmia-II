'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    
    inv = []
    for livro in livros:
        sum = 0
        for idx, num in enumerate(livros[livro]):
            
            if idx == 0 or idx % 2 == 0:
                sum += int(num)*1
            else:
                sum += int(num)*3
                
        if sum % 10 != 0 :
            inv.append(livro)
        
    return inv
