while(True):
    h=100
    x=0
    s=100
    for i in range(0,int(input('请输入第几次落地：'))):
        s+=x
        h/=2
        x=2*h
    else:
        print("第%d次落地时经过%.2f米，第%d次反弹高度为%.2f米！"%(i+1,s,i+1,h))


    
