import csv #Импортируем библиотеку для работы с таблицами csv
def GenPass(a,b): #a-Название корабля b-название планеты
    return str(b[-3::-1]+a[1:3:-1]+b[:3:-1]).capitalize()

file=open('space.txt',encoding='UTF-8') 
data=file.read().split('\n') #Открываем файл и разделяем по столбцам
header=data[0] # Новое название столбцов
data.pop(0) #удаляем старое название столбцов
space_uniq_password=open('space_uniq_password.csv','w',encoding='UTF-8')
writer=csv.writer(space_uniq_password)

dataNew=[]
for i in data:
    s=i.split('*')
    dataNew.append(GenPass(s[0],s[1]))
for x in dataNew:
    writer.writerow(s)
