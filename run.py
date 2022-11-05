import random

# now = random.randint(0, 100)

    # # print(now)

    # if now == 1:
    #     print('Привет')
    # elif (now == 2 or now == 18 or now == 19 or now == 28 or now == 38 or now == 40):
    #     print('Пока')
    # elif now == 3:
    #     print('Где ты?')
    # elif now == 4:
    #     print('Всем лежать, работает спецназ!!!!!!!!!!!!!!!')
    # else:
    #     print(':(')


koloda = ['6','7','8','9','10','v','d','k','t']
masti = ['ch','kr','bu','pi']

bito = []
ruka = []

def getCard():
    if len(bito) >= 36:
        return 'колода пуста'
    card = koloda[random.randint(0, len(koloda)-1)]
    mast = masti[random.randint(0, len(masti)-1)]
    karta = card + mast
    if karta in bito:
        karta = getCard()
    # TODO: убрать баг
    bito.append(karta)
    return karta


game = True
while game:
    cont = input('Взять карту?')
    if cont == 'y':
        kart = getCard()
        if kart == 'колода пуста':
            die()
        else:
            print('в вашей руке: ' + ' '.join(ruka))
            ruka.append(kart)
            print('Пришла карта: ' + kart)
    elif cont == 'n':
        print('------------------    ----------------')
        print('-----      -------    -------     ----')
        print('------------------    ----------------')
        print('в вашей руке: ' + ' '.join(ruka))
        #
        print('конец игры')
        game = False

####
# print('---------')
# for i in bito:
#     print(i)
