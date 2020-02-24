list=[]
a,b=1,2
for i in range(0,20):
    list.append(float(b/a))
    k=b
    b=a+b
    a=k
print(list)
print("前20项的和为：%.3f"%sum(list))
