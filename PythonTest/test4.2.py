'''
输入两个正整数计算它们的最大公约数和最小公倍数

Version:1.0
Author:Andy
Date:2020/09/08
'''
a = int(input('int a ='))
b = int(input('int b ='))
for i in range(0,a):
    subi = a-i
    if a%subi==0:
        if b%subi==0:
            print('%d和%d的最大公约数是:%d'%(a,b,subi))
            break

for j in range(max(a,b),a*b+1):
    if j % a == 0 and j % b == 0:
        print('%d和%d的最小公倍数是：%d'%(a,b,j))
        break


