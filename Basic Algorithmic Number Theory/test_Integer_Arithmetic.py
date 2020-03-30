# coding=utf-8

import gmpy2
import Integer_Arithmetic as d
import random
import os


def test(myFunc, gmpy2Func, N, gmpy2Func_name):
    """
    :param N:  测试例子的个数
    """

    argNum = myFunc.func_code.co_argcount

    for i in xrange(N):
        if argNum == 1:
            bigNum = 500000000000000
            arg = random.randrange(-bigNum, bigNum)
        else:  # if argNum == 2

            bigNum = 5000000000000000000000000

        for j in xrange(argNum):
            # print argNum
            # print j
            arg1 = random.randrange(-bigNum, bigNum)
            arg2 = random.randrange(-bigNum, bigNum)

        if argNum == 1:
            myResult = myFunc(arg)
            gmpy2Result = gmpy2Func(arg)
        else:  # if argNum == 2
            myResult = myFunc(arg1, arg2)
            gmpy2Result = gmpy2Func(arg1, arg2)

        if myResult != gmpy2Result:
            print "%s is wrong" % myFunc.func_name

            if argNum == 1:
                print "{}({}) = {}.".format(myFunc.func_name, arg, myResult)
                print "{}({}) = {}.".format(gmpy2Func_name, arg, gmpy2Result)
            else:  # if argNum == 2:
                if myResult == None:
                    print "{}({},{}) = {}.".format(gmpy2Func_name, arg1, arg2, gmpy2Result)
                else:
                    print "{}({},{}) = {}.".format(myFunc.func_name, arg1, arg2, myResult)
                    print "{}({},{}) = {}.".format(gmpy2Func_name, arg1, arg2, gmpy2Result)
            os.system("pause")


def test_isPrime(N):
    gmpy2Func_name = 'gmpy2.is_prime'
    test(d.isPrime, gmpy2.is_prime, N, gmpy2Func_name)


def test_gcd(N):
    gmpy2Func_name = 'gmpy2.gcd'
    test(d.gcd, gmpy2.gcd, N, gmpy2Func_name)


def test_gcdext_v1(N):
    gmpy2Func_name = 'gmpy2.gcdext'
    test(d.gcdext_v1, gmpy2.gcdext, N, gmpy2Func_name)


def test_gcdext_v2(N):
    gmpy2Func_name = 'gmpy2.gcdext'
    test(d.gcdext_v2, gmpy2.gcdext, N, gmpy2Func_name)


if __name__ == '__main__':
    N = 100000

    # test_isPrime(N)
    # print "isPrime() tested."
    test_gcd(N)
    print "gcd() tested."
    test_gcdext_v1(N)
    print "gcdext_v1() tested."
    test_gcdext_v2(N)
    print "gcdext_v2() tested."
    print "All functions are tested.No exceptions."
