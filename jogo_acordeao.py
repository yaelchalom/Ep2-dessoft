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
        