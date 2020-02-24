PeachList=[]
s=1
for i in range(0,10):
    PeachList.append(s)
    s=(s+1)*2
PeachList.sort(reverse=True)
print(PeachList)
print('第一天共摘桃子：',PeachList[0])
