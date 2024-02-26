file=open('space.txt',encoding='UTF-8') 
data=file.read().split('\n') #Открываем файл и разделяем по столбцам
data.pop(0) # Убираем название столбцов
dataNew=[] #Создаем список и прогоняем данные стобцов
for i in data:
    s=i.split('*')
    dataNew.append(s)
dataNew=sorted(dataNew,key=lambda x: x[0][5:]) #Сортировка
c=0
for q in dataNew:
    print(q[0])
    c+=1
    if c==10: break #Выводим названия пока не достигнем 10 названий

