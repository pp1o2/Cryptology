# coding=utf-8

from Integer_Arithmetic import *


def mod_add(a, b, m):
    return (a + b) % m

def mod_sub(a, b, m):
    return (a - b) % m

def mod_mul(a, b, m):
    return a * b % m

    '''
    # 可用以下代码提升效率:
     a = a % m
    res = 0
    while b != 0:
        if b & 1:
            res = (res + a) % m
        b >>= 1
        a = (2 * a) % m
    
    return res
    '''

def mod_inv(a, m):
    gcd, res, _= gcdext(a,m)
    assert gcd == 1

    return res % m

def mod_pow(a, b, m, phi_m = 0):
    """
    :param phi_m:  若已知 φ(m)，则可以优化算法
    :return: (a ** b) % m
    """

    a = a % m
    res = 1
    if phi_m != 0:
        # 因为根据欧拉定理, a^φ(m) = 1 (mod m), 故此处可对b取余来优化算法
        b = b % phi_m

    if a == 0:
        return 0

    if b == 0:
        return 1

    while b != 0:
        if b & 1:
            res = (res * a) % m
        b >>= 1
        res = res * res % m

    return res

def Legendre(a, p):
    assert is_prime(p)
    a = a % p
    # Euler 判别法
    res = mod_pow(a, (p - 1) // 2, p)

    return res

def LinearCongruenceSolver(a, b, m):
    d = gcd(a, b)
    if b % d != 0:
        return None
    a = a // d
    b = b // d
    m = m // d

    return mod_inv(a, m) * b % m

def mod_sqrt(a, p):
    if a == 0:
        return 0
    assert Legendre(a, p) == 1




# TODO List:
#   Jacobi(a, m)
#   Tonelli_Shanks_Algorithm(**arg)
#   mod_sqrt(a, p) 求解x^2 = a (mod p)，注意p必须是一个素数
#   QuardraticCongruenceSolver(a, b, c, p) 求解 ax^2 + bx + c = 0 (mod p), p必须是素数
#   CRT(ai,mi)      #使用孙子定理求解方程组 x = ai (mod mi), 其中mi可以不互素
#   Miller_Rabin_Algorithm(**arg)



