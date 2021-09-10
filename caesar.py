
def caesar_simple(message,shift,key, desh=False):
    message = message.lower()   #Переводим обе строчные переменные в нижний регистр
    key = key.lower()           #Во избежании конфликтов
    keyset=set(key)             #Делаем из списка множество
    if(len(key)>len(keyset)):   #Проверка ключа - является ли он множеством.
        return "ОШИБКА! В КЛЮЧЕ ПОВТОРЯЮТСЯ БУКВЫ"
    al='абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet=list(al)           #Создание списка алфавита и его копии
    alphabet_notkey=list(al)
    for ch in key:              #Удаление из второго алфавита ключей
        alphabet_notkey.remove(ch)
    newTT=len(alphabet_notkey)  #Длина алфавита без ключа
            #составление нового алфавита
    alphabet_new=alphabet_notkey[newTT-shift:newTT]+list(key)+alphabet_notkey[0:newTT-shift]
    #print(alphabet_new)
    #print(alphabet)
    mes_new=''
    for ch in message:          #Поиск и замена букв в сообщении
        if ch in alphabet:      #В зависимости от того, нам нужен шифратор, или дешифратор
            mes_new+=alphabet[alphabet_new.index(ch)]if desh else alphabet_new[alphabet.index(ch)]
        else:
            mes_new+=ch         #...Кроме тех, которые есть в алфавите


    return mes_new

def caesar_hard(message,key,desh=False):
    message = message.lower() #Перевод сообщения и ключа в нижний регистр
    mes_fin=''
    key = key.lower()
    alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя') #список-алфавит
    #al_plus=[]             #Массив констант для прибавления к буквам.
    #for i in range(len(alphabet)):
    #    al_plus.append(key[i%len(key)])
    for i in range(len(message)):                       #По сообщению
        if message[i] in alphabet:                      #Если буква включена в алфавит
            keynow=alphabet.index(key[i%len(key)])      #номер буквы ключа в алфавите
            if(desh):
                mes_fin+=alphabet[(alphabet.index(message[i]) - keynow+32) % 32]  #разность - дешифратор.
            else:
                mes_fin+=alphabet[(alphabet.index(message[i])+keynow)%32]   #в новое сообщение пишем букву от суммы
        else:
            mes_fin+=message[i]
    #print("алфавит")
    #print(alphabet)
    #print("алфавит,смещенный на %",key)
    #print(al_plus)
    return mes_fin