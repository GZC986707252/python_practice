data=input('请输入3个整数[逗号分隔]：')
a,b,c=(int(i) for i in data.split(','))
m=0
if a>=b:
    m=a
    a=b
    b=m
if a>=c:
    m=a
    a=c
    c=m
elif b>c:
    m=b
    b=c
    c=m
print("3个整数从小到大为：%d,%d,%d"%(a,b,c))
