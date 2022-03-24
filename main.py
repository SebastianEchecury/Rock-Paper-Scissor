import random
import time

def jugar():
    print('r para piedra, p para papel y s para tijera: ', end='')
    opt = ''
    while (opt != 'r' and opt != 'p' and opt != 's'):
        opt = input()
        if opt != 'r' and opt != 'p' and opt != 's':
            print('Ingrese una opcion valida')
    pcOpt = random.choice(['r', 'p', 's'])

    if pcOpt == 'r': print('La maquina eligio piedra')
    elif pcOpt == 'p': print('La maquina eligio papel')
    else: print('La maquina eligio tijera')

    time.sleep(1)

    if opt == 'r':
        if pcOpt == 'r':
            print('Empate')
        elif pcOpt == 'p':
            print('Perdiste')
        else: print('Ganaste!')
    elif opt == 'p':
        if pcOpt == 'r':
            print('Ganaste!')
        elif pcOpt == 'p':
            print('Empate')
        else: print('Perdiste!')
    else:
        if pcOpt == 'r':
            print('Perdiste!')
        elif pcOpt == 'p':
            print('Ganaste')
        else: print('Empate!')
print('Bienvenido a piedra, papel o tijera')
jugar()