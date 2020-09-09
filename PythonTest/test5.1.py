'''
找出所有水仙花数
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身

Version:1.0
Author:Andy
Date:2020/09/08
'''

import math
import test

for i in range(100,1000):
    a = i//100
    b = i % 100 // 10
    c = i % 100 % 10
    if  math.pow(a,3)+math.pow(b,3)+math.pow(c,3) == i:
        print('%d是水仙花数' % i)