#Author : Jakub Bryl

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

import re
first = None
while first not in ['access','trunk']:
     first = input("Enter interface mode (access/trunk):")

pattern = None
while pattern == None:
    second = input("Enter interface type and number(please use shorter form[Fa/Gi/Se]):")
    pattern = re.search('((Fa|Gi|Se)\d{1,2}/\d{1,2})',second)

if first == 'access':
    pattern1 = None
    while pattern1 == None:
        third = input("Enter VLAN number:")
        pattern1 = re.search('^(\d|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|40[0-8][0-9]|409[0-5])$',third)
elif first == 'trunk': #Allowed VLANS => 1 - 4095
    pattern2 = None
    while pattern2 == None:
        third = input("Enter allowed VLANs:")
        pattern2 = re.search('^(\d|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|40[0-8][0-9]|409[0-5])(,(\d|[1-9][0-9]|[1-9][0-9][0-9]|[1-3][0-9][0-9][0-9]|40[0-8][0-9]|409[0-5]))*$',third)


print('\nInterface {}'.format(second))
if first == 'access':
    for i in range(5):
        if i == 1:
            print(access_template[1].format(third))
        else:
            print(access_template[i])


if first == 'trunk':
    for i in range(3):
        if i == 2:
            print(trunk_template[2].format(third))
        else:
            print(trunk_template[i])
