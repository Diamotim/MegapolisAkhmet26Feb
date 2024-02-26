def PribZnach(n,m,t,xd,yd):
    if n>5: x=n+xd
    if n<=5: x=-(n+xd)*4+t
    if m>3: y=m+t+yd
    if m<=3: y=-(n+yd)*m
    return [x,y]


file=open('space.txt', encoding='UTF-8').read()
data=file.split('/n')    #Открываем файл и разделяем по рядам

header=data.pop(0).split('*')   #Первая строка с названиями стобцов
spacenew=[]

for i in data:
    s=i.split('*')
    if s[2]=='0 0':
        s[2]=PribZnach(int(s[0][5]),int(s[0][6]),len(str(s[1])),int(s[3][0:s[3].find(' ')]),int(s[3][s[3].find(' '):]))
    spacenew.append(s)
print(spacenew)
