import sys
import typing

import nomeklatura


def get_name(s):
    pin = nomeklatura.dict_clients.get(s)
    if pin is None:
        print('Няма такова име')
        sys.exit()
    else:
        return pin


def get_pin(real_pin):
    ok = False
    for _ in range(1, 4):
        new_pin = input('Въведете пин:')
        if new_pin == real_pin:
            ok = True
            break
    if not ok:
        print('Картата е блокирана')
        sys.exit()


def balans(name1):
    balans1 = nomeklatura.dict_clients_balans.get(name1)
    print(f'Налична сума: {balans1}')


def teglene(name2):
    tegli_s = float(input('Колко теглите:'))
    client_suma = nomeklatura.dict_clients_balans.get(name2)
    while client_suma < tegli_s:
        tegli_s = float(input('Сумата е повече от наличното. Колко теглите:'))
    new_suma = client_suma - tegli_s
    nomeklatura.dict_clients_balans[name2] = new_suma
    print(f'Налична сума: {new_suma}')
    sys.exit()


def vnos(name3):
    add_s = float(input('Колко внасяте:'))
    client_suma = nomenklatura.dict_clients_balans.get(name3)
    new_suma = client_suma + add_s
    nomenklatura.dict_clients_balans[name3] = new_suma
    print(f'Налична сума: {new_suma}')
    sys.exit()


if __name__ == '__main__':
    name = input('Въведете име:')
    ima_pin = get_name(name)
    get_pin(ima_pin)
    balans(name)
    izbor = int(input('Какво избирате Теглене/Внасяне/Баланс (1/2/3) : '))
    if izbor == 1:
        teglene(name)
    elif izbor == 2:
        vnos(name)
    elif izbor == 3:
        print(f'Налична сума: {balans}')
        sys.exit()