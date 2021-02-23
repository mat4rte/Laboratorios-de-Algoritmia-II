"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""


def hacker(log):
    
    logs = {}           #Lista Intermédia
    logF = []           #Lista Final
    
    for num,mail in log:
        if mail not in logs:
            logs[mail] = [num]
        else:
            logs[mail].append(num)
    print(logs)
    for mail in logs:
        if len(logs[mail]) > 1:
            melhor = logs[mail][0]
            for pos_mail in range(1, len(logs[mail])):
                melhor = combine(melhor, logs[mail][pos_mail])
            logF.append((melhor,mail))
        else:
            logF.append((logs[mail][0],mail))
            
    return sorted(logF, key = lambda x: (x[0].count('*'), x))
    
def combine(num1, num2):
    
    cartao = ""
    for i in range(len(num1)):
        if num1[i] == "*" and num2[i] != "*":
            cartao+=str(num2[i])
        elif num1[i] != "*" and num2[i] == "*":
            cartao+=str(num1[i])
        elif num1[i] == "*" and num2 [i] == "*":
            cartao+=str('*')
        else:
            cartao+=str(num1[i])
    return cartao
