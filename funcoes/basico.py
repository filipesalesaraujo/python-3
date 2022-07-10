def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome}! Voce nem parece ter {idade} anos')

saudacao()
saudacao('Maria')
saudacao('Joao', 33)
saudacao(idade=34)

if __name__ == '__main__':
    saudacao('Ana', idade = 30)

def soma_e_multiplicacao(a, b, x):
    return a + b * x

c = soma_e_multiplicacao(x=10, a=2, b=3)
d = soma_e_multiplicacao(x=20, a=3, b=7)
print(c)
print(d)
print(c + d)