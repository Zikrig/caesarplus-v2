def razl(message):                              #составление строки букв по популярности
    result = [0 for i in range(32)]
    message = message.lower()
    numberch = 0
    #procres = [0.0 for i in range(32)]
    for ch in message:      #общее колличество цифр
        numberch += 1

        if (ord(ch) > 1071 and ord(ch) < 1104):     #символ в русском алфавите?
            result[ord(ch) - 1072] += 1
    #for i in range(32):    # Пересчет колличества букв на проценты
    #    procres[i] = float(100 * result[i] / numberch)
        #print(str(i)+' '+str(result[i])+' '+chr(i+1072))

    popalf = 'оеанитлсвркмудяпьгзыбчжйшхюэцщфъ' #буквы по популярности

    maxr=[]
    newalf = ""
    i = 0
    while (i<32):                                       #список букв по популярности
        letternum = int(result.index(max(result)))      #номер максимальной буквы
        maxr.append(max(result))
        newalf += chr(letternum+1072)
        result[letternum] = -1
        i+=1
    alf=[popalf,newalf]                                 #образец и алфавит по популярности

    return(alf)
def vyr(alf):#перестановка букв в правильном порядке
    if(len(alf)!=32):
        return "Fuck"
    alfold=alf
    newalf=alfold[2]+alfold[20]+alfold[8]+alfold[17]+alfold[13]+alfold[1]+alfold[22]+alfold[18]+alfold[4]+alfold[23]+alfold[10]+alfold[6]+alfold[11]+alfold[3]+alfold[0]+alfold[15]+alfold[9]+alfold[7]+alfold[5]+alfold[12]+alfold[30]+alfold[25]+alfold[28]+alfold[21]+alfold[24]+alfold[29]+alfold[31]+alfold[19]+alfold[16]+alfold[27]+alfold[26]+alfold[14]

    #mgm=""                         #обновление строчки повыше на случай, если обновится строчка "буквы по популярности"
    #for i in range(32):
    #    for p in range(32):
    #        if ord(alfold[p])-1072==i:
    #            print(str(p)+"  "+alfold[p])
    #           mgm+="alfold["+str(p)+"]+"
    #print(mgm)

    return newalf

def rashr(messege,alfs):            #замена букв на их расшифровку
    alf=list('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    newmes=''
    for let in messege:             #но только, если это русские буквы
        if ord(let)<1104 and ord(let)>=1071:
            newmes+=alf[alfs.index(let)]
        else:
            newmes+=let
    return newmes

def zam(alfav,b1, b2):          #Заменить итоговые буквы на более верные
    alf=list(alfav)
    alfv =list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    a1=alfv.index(b1)
    a2=alfv.index(b2)
    c= alf[a1]
    alf[a1]=alf[a2]
    alf[a2]=c
    alfstrnew=''
    for a in alf:
        alfstrnew+=a
    return alfstrnew

