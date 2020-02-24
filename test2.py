L = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print('原始列表为: {}'.format(L))
num = int(input('输入一个数:'))
L.append(num)
for i in range(1, len(L)+1):
    if L[-i] < L[-(i+1)]:
        L[-i], L[-(i+1)] = L[-(i+1)], L[-i]
    else:
        break
print('新的列表为: {}'.format(L))

