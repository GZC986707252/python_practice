list=[]
temp=1
for i in range(1,21):
    for j in range(1,i+1):
        temp*=j
    list.append(temp)
print(list)
print("Sum:",sum(list))
