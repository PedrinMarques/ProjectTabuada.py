#Esse é o ProjectTabuada.py
#Antes de começar, lembre-se de ter o Python instalado em sua máquina.
#Esse projeto faz a tabuada de um número digitado pelo usuário, de 0 a 20.


# =====Início do Código=====

print('Olá senhor(a), seja bem vindo(a)!\nEsse é o ProjectTabuada.py, ele faz tabuadas de 0 a 20.\nPara iníciarmos com o projeto, faça oque se pede. ')

#n = Nome
#Váriavel para guardar o nome do usuário
n=input('Digite o seu nome: ')

print(f'Ok {n}, agora você pode testar o ProjectTabuada.py.')
print('Faça oque pedir abaixo: ')

# =====Desenvolvimento do código=====

#n = Número
#Váriavel para guardar o número do usuário para prosseguir com o codígo
n1 = (input(f'{n}, digite um número: ')) 

#nf = Número Float
#Váriavel para guardar o número em float e prosseguir com a tabuada
nf1 =  None

#nv = Número Válido
#Váriavel para garantir que o número digitado seja válido
nv = False

while nv is False:
    try:
        nf1 = float(n1)
        nv = True
    except:
        print(f'{n}, o número digitado não é válido!')
        nv = False
        n1 = (input(f'{n}, digite outro número, que seja válido: '))
        
    
#t = Tabuada
#Váriavel para fazermos a tabuada
t0 = nf1 * 0
t1 = nf1 * 1
t2 = nf1 * 2
t3 = nf1 * 3
t4 = nf1 * 4
t5 = nf1 * 5
t6 = nf1 * 6
t7 = nf1 * 7
t8 = nf1 * 8
t9 = nf1 * 9
t10 = nf1 * 10
t11 = nf1 * 11
t12 = nf1 * 12
t13 = nf1 * 13
t14 = nf1 * 14
t15 = nf1 * 15
t16 = nf1 * 16
t17 = nf1 * 17
t18 = nf1 * 18
t19 = nf1 * 19
t20 = nf1 * 20

#Tabuada de 0 a 10
print(f'{nf1}.0 = {t0}')
print(f'{nf1}.1 = {t1}')
print(f'{nf1}.2 = {t2}')
print(f'{nf1}.3 = {t3}')
print(f'{nf1}.4 = {t4}')
print(f'{nf1}.5 = {t5}')
print(f'{nf1}.6 = {t6}')
print(f'{nf1}.7 = {t7}')
print(f'{nf1}.8 = {t8}')
print(f'{nf1}.9 = {t9}')
print(f'{nf1}.10 = {t10}')

print(f'Agora {n}, iremos ver a continuação da tabuada de 11 a 20. ')

#Tabuada de 11 a 20
print(f'{nf1}.11 = {t11}')
print(f'{nf1}.12 = {t12}')
print(f'{nf1}.13 = {t13}')
print(f'{nf1}.14 = {t14}')
print(f'{nf1}.15 = {t15}')
print(f'{nf1}.16 = {t16}')
print(f'{nf1}.17 = {t17}')
print(f'{nf1}.18 = {t18}')
print(f'{nf1}.19 = {t19}')
print(f'{nf1}.20 = {t20}')
# =====Fim do código=====

#f = Feedback
#Váriavel para guardar o feedback do usuário
f = None

while f is None:
    f=input(f'{n}, oque você achou do projeto ProjectTabuada.py?\nDigite "Sim" se gostou ou "Não" se não gostou: ').lower()

    if f == 'sim':
        print('Fico feliz que tenha gostado!')
        break
    elif f == 'não':
        print('Que pena que não tenha gostado, comente no Github oque posso melhorar! ')
        break
    else:
        print('Resposta inválida, tente novamente!')

print(f'Obrigado por testar o ProjectTabuada.py, {n}, até a próxima!')

#Para quem esta analisando o código, espero que tenha gostado! :)
#Qualquer dúvida, entre em contato comigo pelo Github:
#Tenho 14 anos e estou aprendendo a progamar, espero que tenham gostado :)
#Até mais!