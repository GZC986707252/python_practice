def Total(n):
    if n==1 or n==0:
        return 1
    else:
        return n*Total(n-1)
print('该数的阶乘是：',Total(int(input("请输入一个整数："))))
