import random
import todas_as_funções
iiii = 0
print('Paciência Acordeão\n==================\nBem Vindo(a) ao jogo de Paciência Acordeão!\n)
b = input('')
if b == '':
    aperta = True
while aperta == True:
    baralho = todas_as_funções.cria_baralho()
    mover = True
    while mover == True:
        mover = todas_as_funções.possui_movimentos_possiveis(baralho)
        if mover == False:
            break
        lista_n = range(1, len(baralho)+1)
        print('Atualmente o baralho se encontra em:')
        for i in range(max(lista_n)):
            ind = lista_n[i]
            cart = baralho[i]
            print('{0}. {1}'.format(ind, cart))
         a = input('Escolha uma carta (digite um número entre 1 e {}):)' .format(max(lista_n)))
        while int(a) not in range(1, (max(lista_n)+1)):
            a = input('Posição inválida. Digite um número entre 1 e {}, por favor): '.format(max(lista_n)))
        indice = int(a) - 1
    l   ista_movimento = todas_as_funções.lista_movimentos_possiveis(baralho, indice)
        carta_selecionada = baralho[indice]
        while lista_movimento == []:
            a = int(input('Movimento não pode ser realizado, insire um número e 1 a {}: '.format(max(lista_movimento))))
            if 0 <= a < max(lista_n):
                break
            mover = todas_as_funções.possui_movimentos_possiveis(baralho)
            if mover == False:
                iiii = 1
                break
            indice = int(a)-1
            lista_movimento = todas_as_funções.lista_movimentos_possiveis(baralho, indice)
        if iiii == 1:
            break
        
        