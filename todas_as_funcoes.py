def cria_baralho():
    baralho = ['A♥️', 'K♥️', 'Q♥️', 'J♥️', '10♥️', '9♥️', '8♥️', '7♥️', '6♥️', '5♥️', '4♥️','3♥️', '2♥️','A♠️', 'K♠️', 'Q♠️', 'J♠️', '10♠️','9♠️', '8♠️', '7♠️', '6♠️', '5♠️', '4♠️', '3♠️', '2♠️','A♦️','K♦️','Q♦️', 'J♦️', '10♦️', '9♦️', '8♦️', '7♦️', '6♦️', '5♦️', '4♦️', '3♦️', '2♦️', 'A♣️', 'K♣️', 'Q♣️', 'J♣️', '10♣️', '9♣️', '8♣️', '7♣️', '6♣️', '5♣️', '4♣️', '3♣️', '2♣️']
    return baralho

def extrai_naipe(carta):
    baralho = ['A♥️', 'K♥️', 'Q♥️', 'J♥️', '10♥️', '9♥️', '8♥️', '7♥️', '6♥️', '5♥️', '4♥️','3♥️', '2♥️','A♠️', 'K♠️', 'Q♠️', 'J♠️', '10♠️','9♠️', '8♠️', '7♠️', '6♠️', '5♠️', '4♠️', '3♠️', '2♠️','A♦️','K♦️','Q♦️', 'J♦️', '10♦️', '9♦️', '8♦️', '7♦️', '6♦️', '5♦️', '4♦️', '3♦️', '2♦️', 'A♣️', 'K♣️', 'Q♣️', 'J♣️', '10♣️', '9♣️', '8♣️', '7♣️', '6♣️', '5♣️', '4♣️', '3♣️', '2♣️']
    if carta[0] + carta[1] == '10': #ou carta[:,2]
            return carta[2]
    return carta[1]

def extrai_valor(carta):
    if carta[0] + carta[1] == '10':
        return '10'
    return carta[0]
    
def lista_movimentos_possiveis(baralho, indice):
   lista_naipe = []
   lista_valor = []
   resultado = []
   for i in range(len(baralho)):
       naipe = extrai_naipe(baralho[i])
       valor = extrai_valor(baralho[i])
       lista_naipe.append(naipe)
       lista_valor.append(valor)
   if indice == 0:
        return resultado
   else:
       if lista_valor[indice] == lista_valor[indice-1] or lista_naipe[indice] == lista_naipe[indice-1]:
           resultado.append(1)
       if indice > 2:
           if lista_valor[indice] == lista_valor[indice-3] or lista_naipe[indice] == lista_naipe[indice-3]:
               resultado.append(3)
   return resultado

def empilha(carta, indice, destino):
    carta_selecionada = carta[indice]
    carta[destino] = carta_selecionada
    del(carta[indice])
    return carta

def possui_movimentos_possiveis(baralho):
    existe = 0
    for i in range(0,len(baralho)-1):
        movimento = lista_movimentos_possiveis(baralho, i)
        if movimento == []:
            existe += 0
        else:
            existe += 1
    if existe != 0:
        return True
    else:
        return False