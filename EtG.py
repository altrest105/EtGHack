import pymem
import pymem.process
from pymem.ptypes import RemotePointer

#Получение номера функции для выполнения
def get_command():
    print('''
Choose function:
    1. MoneyGive
    2. KeysGive
    3. VoidsGive
    4. HealthGive
    5. MaxHealth
    6. Change X coordinate
    7. Change Y coordinate
    8. Exit''')
    command = input()
    return command

#Изменение значения количества денег
def money_give():
    amount = int(input("Enter amount of money: "))
    pm.write_int(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x40, 0x80, 0x28, 0x30, 0x198, 0x1C]), amount)

#Изменение значения количества ключей
def keys_give():
    amount = int(input("Enter amount of keys: "))
    pm.write_int(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x40, 0x80, 0x28, 0x30, 0x198, 0x20]), amount)

#Изменение значения количества пустышек
def voids_give():
    amount = int(input("Enter amount of voids: "))
    pm.write_int(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x0, 0x8, 0x8, 0x98, 0x28, 0x30, 0x568]), amount)

#Изменение значения здоровья
def health_give():
    amount = float(input("Enter amount of health: "))
    pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0x50, 0x118]), amount)

#Изменение значения количества здоровья
def max_health():
    amount = float(input("Enter amount of max health: "))
    pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0x50, 0x114]), amount)

#Изменение координаты X
def x_change():
    side = input('Choose a side (left/right): ')

    if side == 'right':
        mode = input('Enter the mode (auto/input): ')
        if mode == 'auto':
            curr_x = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))
            print(f'Your current X coordinate = {curr_x}')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]), curr_x + (10**(-43)))
            print(f'Your new X coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))}')
        if mode == 'input':
            curr_x = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))
            print(f'Your current X coordinate = {curr_x}')
            delta_x = input('Enter the change: ')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]), curr_x + (delta_x**(-43)))
            print(f'Your new X coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))}')

    elif side == 'left':
        mode = input('Enter the mode (auto/input): ')
        if mode == 'auto':
            curr_x = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))
            print(f'Your current X coordinate = {curr_x}')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]), curr_x - (10**(-43)))
            print(f'Your new X coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))}')
        if mode == 'input':
            curr_x = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))
            print(f'Your current X coordinate = {curr_x}')
            delta_x = input('Enter the change: ')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]), curr_x - (delta_x**(-43)))
            print(f'Your new X coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x170]))}')

    else:
        print('Unkown command, try again!')

#Изменение координаты Y
def y_change():
    side = input('Choose a side (up/down): ')

    if side == 'up':
        mode = input('Enter the mode (auto/input): ')
        if mode == 'auto':
            curr_y = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))
            print(f'Your current Y coordinate = {curr_y}')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]), curr_y + (10**(-43)))
            print(f'Your new Y coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))}')
        if mode == 'input':
            curr_y = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))
            print(f'Your current Y coordinate = {curr_y}')
            delta_y = input('Enter the change: ')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]), curr_y + (delta_y**(-43)))
            print(f'Your new Y coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))}')

    elif side == 'down':
        mode = input('Enter the mode (auto/input): ')
        if mode == 'auto':
            curr_y = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))
            print(f'Your current Y coordinate = {curr_y}')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]), curr_y - (10**(-43)))
            print(f'Your new Y coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))}')
        if mode == 'input':
            curr_y = pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))
            print(f'Your current Y coordinate = {curr_y}')
            delta_y = input('Enter the change: ')
            pm.write_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]), curr_y - (delta_y**(-43)))
            print(f'Your new Y coordinate = {pm.read_float(getPointerAddress(base_address + 0x0144EBB8, offsets = [0x8, 0x98, 0x28, 0x30, 0x18, 0xC8, 0x174]))}')

    else:
        print('Unkown command, try again!')

#Получение адреса
def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset



#Подключение к игре
print('Cheat for "Enter The Gungeon" by @altrest105')
pm = pymem.Pymem("EtG.exe")
base_address = pymem.process.module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll #UnityPlayer.dll
base_address_mono = pymem.process.module_from_name(pm.process_handle, "mono.dll").lpBaseOfDll

#Проверка на подключение
if pm:
    print('Connected to EtG.exe')
else:
    print('EtG.exe is not found!')
    exit()

#Выбор функции
while True:
    command = get_command()
    if (command == '1'):
        money_give()
    elif (command == '2'):
        keys_give()
    elif (command == '3'):
        voids_give()
    elif (command == '4'):
        health_give()
    elif (command == '5'):
        max_health()
    elif (command == '6'):
        x_change()
    elif (command == '7'):
        y_change()
    elif (command == '8'):
        exit()
    else:
        print('Unkown command, try again!')
        command = get_command()