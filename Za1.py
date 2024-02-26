def PribZnach(n,m,t,xd,yd):
    if n>5: x=n+xd
    if n<=5: x=-(n+xd)*4+t
    if m>3: y=m+t+yd
    if m<=3: y=-(n+yd)*m
    return [x,y]

import csv                      #Импортируем библиотеку для работы с таблицой

file=open('space.txt', encoding='UTF-8')
data=file.read().split('/n')    #Открываем файл и разделяем по рядам

header=data.pop(0).split('*')   #Первая строка с названиями стобцов
spacenew=open('spacenew.csv','w')
writer=csv.writer(spacenew)
writer.writerow(header)
print(data)
for i in data:
    s=i.split('*')
    print(s)
