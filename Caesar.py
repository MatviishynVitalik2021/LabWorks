alfavit_UA = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
smeshenie = int(input('Ключ: '))
message = input("Текс для шифрування: ").upper()
itog = ''
for i in message:
        mesto = alfavit_UA.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_UA:
            itog += alfavit_UA[new_mesto]
print (itog)
