# coding=utf-8

import gmpy2

def bad_is_prime(a):
    """经典判素方法，对于大整数不实用"""
    if a == 1:
        return False
    if a < 0:
        a = -a

    for i in xrange(2, int(gmpy2.sqrt(a))):
        if a % i == 0:
            return False
    return True

def is_prime(a,n = 25):    # TODO: 使用Miller-Rabin算法 进行概率判素
    """

    :param a:   待判定的数
    :param n:   素性测试次数。 若测试通过n次，则 a不是素数的概率 < 0.25 ** n
    """
    return True

def gcd(a, b):
    """欧几里得算法求最大公约数"""
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        a, b = b, a

        # Now a>=b>=0
    if b == 0:
        return 0
    # 此段 可替换成下面注释段
    while a % b != 0:
        a = a % b
        a, b = b, a
    return b

    '''
    while b != 0:       
        a, b = b, a % b
    return a    
    '''


def lcm(a, b):
    """求解最小公倍数,运用公式 lcm[a,b] = ab/gcd(a,b)"""
    result = (a * b) // gcd(a, b)
    if result > 0:
        return result
    else:
        return -result


def ex_gcd_v1(a, b):
    """
    求解 ax+by = gcd 中的 gcd,x,y
    要求 a > b >= 0
    扩展欧几里得算法的循环实现，
    直接照搬书上的写法
    """
    (X1, X2, X3) = (1, 0, a)
    (Y1, Y2, Y3) = (0, 1, b)

    while Y3 != 0:
        Q = X3 // Y3
        (T1, T2, T3) = (X1 - Q * Y1, X2 - Q * Y2, X3 - Q * Y3)
        (X1, X2, X3) = (Y1, Y2, Y3)
        (Y1, Y2, Y3) = (T1, T2, T3)

    # return gcd,x,y
    return X3, X1, X2


def ex_gcd_v2(a, b):
    """
    求解 ax+by = gcd 中的 gcd,x,y
    要求 a > b >= 0
    扩展欧几里得算法的递归实现
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = ex_gcd_v2(b, a % b)
        x, y = y, x - (a // b) * y
        return gcd, x, y


def gcdext(a, b, mode=0):
    """
    求解任意的 ax+by = gcd
    若有解 返回gcd,x,y，若无解 返回None
    mode = 0为调用循环算法，1为调用递归算法
   返回 gcd(a,b),x,y。其中ax+by = gcd(a,b)
    """

    # sign_a, sign_b = 1, 1
    #   if a < 0:
    #       a = -a
    #        sign_a = -1
    #    if b < 0:
    #        b = -b
    #        sign_b = -1

    # exchanged = False               #若a，b交换过，则输出x，y也要交换
    #
    # if a == b:
    #     print "gcdext(a,b):  |a|与|b|不应相等"
    #     return None
    # if a < b:
    #     exchanged = True
    #     a, b = b, a

    if mode == 0:
        (gcd, x, y) = ex_gcd_v1(a, b)
    if mode == 1:
        (gcd, x, y) = ex_gcd_v2(a, b)

    # if exchanged is True:
    #     x, y = y, x
    #
    if gcd < 0:
        gcd = (-1) * gcd
        x = (-1) * x
        y = (-1) * y

    return (gcd, x, y)


'''
为方便测试故编写gcdext_v1 gcdext_v2
'''


def gcdext_v1(a, b):
    # 调用欧几里得算法的循环形式
    return gcdext(a, b, 0)


def gcdext_v2(a, b):
    # 调用欧几里得算法的递归形式
    return gcdext(a, b, 1)

# TODO List:
#   is_prime(a)
#   next_prime(a)
#   last_prime(a)