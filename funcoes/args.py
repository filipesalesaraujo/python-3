def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


s = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(s)


def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'


resultado = resultado_final(nome='Pedro', nota=6.3)
print(resultado)
