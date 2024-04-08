text_user = input('Введите строку: ')

revers = text_user[text_user.find('h') + 1 : text_user.rfind('h')]

text_user = revers[::-1]

print("Развёрнутая последовательность между первым и последним h:", text_user)
