"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    
    prefs_tup = [(k, v) for k, v in prefs.items()]
    prefs_tup.sort(key = lambda x:x[0])
    escolhidas = []
    n_alocados = []
    
    for aluno in prefs_tup:
        for proj in aluno[1]:
            if proj not in escolhidas:
                escolhidas.append(proj)
                break
            elif aluno[1].index(proj) == len(aluno[1])-1:
                n_alocados.append(aluno[0])
    
    
    return n_alocados
