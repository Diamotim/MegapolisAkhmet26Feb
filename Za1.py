#Создаем функцию для нахождения приблизительных координат корабля
def PribZnach(n,m,t,xd,yd):
    if n>5: x=n+xd
    if n<=5: x=-(n+xd)*4+t
    if m>3: y=m+t+yd
    if m<=3: y=-(n+yd)*m
    return [x,y]


file=open('space.txt', encoding='UTF-8').read().strip()
data=file.split('\n')    #Открываем файл и разделяем по рядам

header=data.pop(0).split('*')   #Первая строка с названиями стобцов
space_new=open('space_new.txt','w',encoding='UTF-8')
space_new.write(str(header).replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",'*')+'\n') #Создаем файл и записываем названия столбцов как первую строчку

#Перебераем строки из файла space.txt
for i in data:
    s=i.split('*')
    if s[2]=='0 0':
        s[2]=str(PribZnach(int(s[0][5]),int(s[0][6]),len(str(s[1])),int(s[3][0:s[3].find(' ')]),int(s[3][s[3].find(' '):]))).replace(', ',' ') # Изменяем 3 столбик если координаты корабля равны "0 0"
    space_new.write(str(str(s).replace('[','').replace(']','').split(', ')).replace('[','').replace(']','').replace('"','').replace("'",'').replace(", ",'*')+'\n') #Записываем в файл
    if s[0][3]=='V': print(s[0]+' - '+'('+str(s[2][:s[2].find(' ')]).replace('[','').replace(']','')+str(s[2][s[2].find(' '):]).replace('[','').replace(']','')+')') #Выводим название корабля вместе с его координатами
space_new.close() #Закрываем файл для редактирования

