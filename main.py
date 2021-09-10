import razlich,menu
from caesar import caesar_simple as cs
import matplotlib.pyplot as pyp
from bukva import bukva as Letter
knga=open('kniga.txt','r',encoding='utf-8')
messege=knga.read()
knga.close()

#res=razl.dvazl(messege)
#for a in range(32):
#    for b in range(32):
#        if(res[a][b]>90):
#            print(str(res[a][b])+' - столько сочетаний букв '+chr(a+1072)+chr(b+1072))

#pyp.imshow(res)
#pyp.show()
print("меню?y/n")
op=input()
if(op=='y'):
    menu.shifr()

knga=open('shifr.txt','w',encoding='utf-8')
shifr_book = cs(messege.lower(),6,'утки')
knga.write = shifr_book
knga.close()


deltab=[]
alfes = razlich.razl(shifr_book)    #поиск алфавита
newalf=razlich.vyr(alfes[1])        #выравнивание алфавита в правильном порядке

newmes=razlich.rashr(shifr_book,newalf) #расшифровка с помощью нового алфавита
i='a'
while(i!=''):
    print(newmes[:400])
    print("Если вы догадались о букве, введите ее так:'а б'. Тогда а в сообщении заменится б")
    print("Если вы просто хотите увидеть полную расшифровку, просто нажмите Enter")
    print("Текущий алфавит - "+newalf)
    i = input()
    if len(i)==3 and i[1]==' ':     #проверка соответствия формату
        ain = ord(i[0])-1072        #порядковый номер буквы в алфавите
        bin = ord(i[2])-1072
        if ain>=0 and ain<33 and bin>=0 and bin<33:
            newalf = razlich.zam(newalf,i[0],i[2])      #новый алфавит (две буквы поменяны)

            newmes = razlich.rashr(shifr_book, newalf)  #заново расшифровываем

print(newmes)