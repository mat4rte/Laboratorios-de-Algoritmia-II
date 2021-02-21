'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    fatores = []
    i = 2
    while n >= 1 and i <= n:
        if n % i == 0:
            if i not in fatores:
                fatores.append(i)
            else:
                n = n // i
        else:
            i+=1
    return sum(fatores)
    
