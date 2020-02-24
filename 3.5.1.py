date = input("输入年月日(yyyy-mm-dd):")
y,m,d = (int(i) for i in date.split('-'))
print('y=%d,m=%d,d=%d'%(y,m,d))
sum=0
special = (1,3,5,7,8,10)
for i in range(1,int(m)):
    if i == 2:
        if y%400==0 or (y%100!=0 and y%4==0):
            sum+=29
        else:
            sum+=28
    elif(i in special):
        sum+=31
    else:
        sum+=30
sum+=d
print("这一天是一年中的第%d天"%sum)
