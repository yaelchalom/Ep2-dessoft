import random
import todas_as_funcoes
iiii = 0
print("Bem Vindo(a) ao jogo de Paciência Acordeão!")
a = input('')
if a == '':
    aperta = True
while aperta == True:
    baralho = todas_as_funcoes.cria_baralho()
    mover = True
    while mover == True:
        mover = todas_as_funcoes.possui_movimentos_possiveis(baralho)
        if mover == False:
            break
        lista_n = range(1, len(baralho)+1)
        print('Atualmente o baralho se encontra em:')
        for i in range(max(lista_n)):
            indi = lista_n[i]
            cart = baralho[i]
            print('{0}. {1}'.format(indi, cart))
        a = input('Escolha uma carta (digite um número entre 1 e {}): '.format(max(lista_n)))
        while int(a) not in range(1, (max(lista_n)+1)):
            a = input('Posição inválida. Digite um número entre 1 e {}): '.format(max(lista_n)))
        indice = int(a) - 1
        lista_movimento = todas_as_funcoes.lista_movimentos_possiveis(baralho, indice)
        carta_selecionada = baralho[indice]
        while lista_movimento == []:
            a = int(input('Movimento não pode ser realizado, insire outro número de 1 a {}: '.format(max(lista_n))))
            if 0 <= a < max(lista_n):
                break
            mover = todas_as_funcoes.possui_movimentos_possiveis(baralho)
            if mover == False:
                iiii = 1
                break
            indice = int(a) - 1
            lista_movimento = todas_as_funcoes.lista_movimentos_possiveis(baralho, indice)
        if iiii == 1:
            break
        if lista_movimento == [1]:
            carta_antecipada = baralho[indice-1]
            baralho = todas_as_funcoes.empilha(baralho, indice, (indice-1))
        if lista_movimento == [3]:
            carta_3_antecipada = baralho[indice-3]
            baralho = todas_as_funcoes.empilha(baralho, indice, (indice-3))
        if lista_movimento == [1, 3]:
            carta_antecipada = baralho[indice-1]
            carta_3_antecipada = baralho[indice-3]
            print('Em qual carta deseja empilhar o {}?'.format(carta_selecionada))
            print('1. {}'.format(carta_antecipada))
            print('2. {}'.format(carta_3_antecipada))
            n_dig = int(input('Digite o número 1 ou 2:'))
            if n_dig == 1:
                baralho = todas_as_funcoes.empilha(baralho, indice, (indice-1))
            if n_dig == 2:
                baralho = todas_as_funcoes.empilha(baralho, indice, (indice-3))
    if len(baralho) == 1:
        print('Você venceu!!')
    if len(baralho) != 1:
        print('Você perdeu!')
    repete = input('Gostaria de jogar novamente (sim/não)? ')
    if repete == 'sim':
        aperta = True
    if repete != 'sim':
        aperta = False
            