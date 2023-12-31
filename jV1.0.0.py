from random import randint

def mainf():
    print('\033[1;33mLuta 1x1 contra The Mega of The Blaster of The World')
    print('Você tem 10 de vida e causa 3 de dano contra ele com 25 de vida e causa 4 de dano')
    print('Você tem 3 poções de cura que curam 4 pontos de vida')
    print('Você e o boss têm 10% de chance de dar e receber críticos, causando o dobro de dano')
    print('Você tem 75% de chance de se esquivar, mas você da 2 de dano e se você não se esquivar você toma 3 de dano')
    print('Se você conseguir 2 ataque seguidos você usa o super causando 5 de dano')
    print('Tem 10% de chance de você ou o monstro se esquivar automáticamente\033[m')
    def vidaf():
        vida_jogador = 10
        vida_mostro = 25
        cura = 3
        tot = 0
        super = []

        ataque = 'a'
        chance_esquiva = 0
        while ataque != 'p' and vida_jogador > 0:
            while vida_mostro != 0 and vida_jogador > 0:
                ataque = str(input('Aperte p para atacar ou e para esquivar: ')).lower()
                if ataque == 'e':
                    chance_esquiva = randint(1, 3)
                    lado = 'a'
                    while lado != 'esquerda' or lado != 'direita':
                        lado = str(input('direita ou esquerda: ')).lower()
                        if lado[0] == 'd':
                            if chance_esquiva == 1 or chance_esquiva == 2:
                                vida_mostro -= 2
                                print(f'\033[1;34mVocê se esquivou para a direita e deu 2 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            break
                        elif lado[0] == 'e':
                            if chance_esquiva == 1 or chance_esquiva == 2:
                                vida_mostro -= 2
                                print(f'\033[1;34mVocê se esquivou para a esquerda e deu 2 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            break
                        else:
                            print('erro')
                tot += 1
                if tot > 1 and vida_jogador < 10:
                    if cura > 0 and vida_jogador <= 6 and vida_jogador >=1 :
                        while True:
                            poçao = str(input(f'\033[1;32mVocê tem {cura} poções de cura. Precione 1 para tomar uma poção de cura e 2 para não tomar:\033[m '))
                            if poçao == '1':
                                cura -= 1
                                vida_jogador += 4
                                print(f'Você usou uma poção de cura. Poções restantes: {cura}')
                                print(f'\033[1;36mVocê recuperou 4 pontos de vida\033[m')
                                break
                            elif poçao == '2':
                                break
                            else:
                                print('\033[1;31mErro: Digite "1" para tomar poção ou "2" para não tomar./033[m')
                if ataque != 'p' and (chance_esquiva != 1 or chance_esquiva != 2 or chance_esquiva != 3):
                    continue
                else:   
                    chance_desvio_automatico = randint(1, 10)
                    chance_acerto_monstro = randint(0,1)
                    chance_acerto_jogador = randint(0,1)
                    critico_pessoa = randint(1, 10)
                    #desvio automatico
                    if chance_desvio_automatico == 1:
                        c = vida_jogador
                        print(f'\033[1;36mVocê desviou | Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                    elif chance_desvio_automatico == 2:
                        d = vida_mostro
                        print(f'\033[1;31mO monstro desviou | Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                    if critico_pessoa == 1 and chance_desvio_automatico != 2:
                        vida_mostro -= 6    
                        print(f'\033[1;35mVocê deu um CRÍTICO de 6 de dano\033[m.')
                        print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}') 
                    else:
                        if chance_acerto_monstro == 0 and chance_desvio_automatico != 2:  
                            if super.count(1) < 3:  
                                vida_mostro -= 3
                                print(f'\033[1;32mO monstro tomou 3 de dano\033[m')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')   
                            #ataque normal pessoa 
                            super.append(1)
                            print(f'\033[1;36m{super.count(1)}/2 Para carregar o super\033[m')
                            if super.count(1) == 2:
                                vida_mostro -= 5
                                super.clear()
                                print(f'\033[1;35mVocê usou o super Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')                      
                    if vida_mostro <= 0:
                        print(f'\033[1;34mVocê venceu meus parabéns 🥳😎\033[m')
                        break
                    else:
                        critico_boss = randint(1,10)
                        if critico_boss == 1 and chance_desvio_automatico != 1 and chance_acerto_jogador != 0 and super.count(1) != 1 and critico_pessoa != 1:
                                #ataque crítico
                            vida_jogador -= 8
                            print(f'\033[1;31mVocê tomou um CRÍTICO de 8 de dano\033[m.')
                            print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                        elif chance_acerto_monstro == 1 and chance_desvio_automatico != 1 and critico_pessoa != 1:
                            #ataque normal boss
                            #talvez o bug aqui
                            super.append(0) 
                            if 1 in super:
                                super.clear()
                            vida_jogador = vida_jogador - 4
                            print(f'\033[1;31mVocê tomou 4 de dano\033[m.')
                            print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                if vida_jogador <= 0:
                    print('\033[0;31mVocê perdeu que pena... 😢🙁\033[m')
                    break
    vidaf()

def modos():
    modos = str(input('qual modo você irá escolher? [fácil/médio/dificil?]'))
    if modos == 'fácil':
        mainf()

modos()