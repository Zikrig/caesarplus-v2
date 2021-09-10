from caesar import caesar_simple as cs
from caesar import caesar_hard as ch
def shifr():
    print("Введите вашу фразу:")
    phrase = input()
    print("Это Фёдор Гризик, и если это не я показываю вам лабу, то у кого-то проблемы)")
    print("Y для простого шифра. N для сложного.")

    if (input().lower() == "n"):
        what_bool = False
    else:
        what_bool = True
    print("Y для шифратора. N для дешифратора.")

    if (input().lower() == "n"):
        dash_bool = True
    else:
        dash_bool = False
    if (what_bool):
        print("Введите смещение:")
        shift = int(input())
        print("Введите ключ (НЕ ПОВТОРЯЙТЕ БУКВЫ):")
        key = input()
        print(cs(phrase, shift, key, dash_bool))
    else:
        print("Введите ключ")
        key = input()
        print(ch(phrase, key, dash_bool))
    pass
