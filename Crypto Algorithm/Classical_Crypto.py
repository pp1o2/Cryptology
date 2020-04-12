# coding=utf-8
import os
from gmpy2 import gcd, invert


# -----------------------  shift cipher

def shift_enc(k, m):
    """
        Do shift cipher encryption.
        Calculate ci: ci ≡ mi+k (mod 26)

    :param int k: Key. (0<k<26)
    :param str m: Plaintext.
    :return str c: Ciphertext.
    """

    assert 0 < k < 26

    c = ""
    ci = ""
    for mi in m:
        if mi.islower():
            ci = chr((ord(mi) - 97 + k) % 26 + 97)
        elif mi.isupper():
            ci = chr((ord(mi) - 65 + k) % 26 + 65)
        else:
            ci = mi
        c += ci

    return c

def shift_dec(k,c):
    """
        Do shift cipher decryption.
        Calculate mi ≡ ci-k (mod 26)

    :param int k: Key. (0<k<26)
    :param str c: Ciphertext.
    :return str m: Plaintext.
    """

    assert 0 < k < 26

    m = ""
    mi = ""
    for ci in c:
        if ci.islower():
            mi = chr((ord(ci) - 97 - k) % 26 + 97)
        elif ci.isupper():
            mi = chr((ord(ci) - 65 - k) % 26 + 65)
        else:
            mi = ci
        m += mi
    return m

def caeser_enc(m):
    return shift_enc(3,m)

def caeser_dec(c):
    return shift_dec(3,c)

'''
Got two ways to break the shift cipher :
    1.Brute force , for there are only 26 possible keys 
    
    2.Frequency analysis , for different letters appear in different frequency
    (Frequency analysis can help us to solve simple substitution ciphers)
'''

def shift_break_by_brute_force(c):
    """
    Print candidate plaintexts.Use ENTER key to change

    :param c: cipher text to be decrypted
    :return: no return
    """

    k = 1
    while True:
        print "\nPress ENTER change cancidate plaintexts."
        candidate = shift_dec(k, c)
        print "\nAssume key = %d\n" %k
        print "%s" %candidate

        os.system("pause")
        k = (k + 1) % 26

# TODO: shift_break_by_frequency_analysis(c)

'''
Just use this website for frequency analysis: https://quipqiup.com/ 
It can solve simple substitution ciphers.
'''

# -----------------------  affine cipher

def affine_enc(m, *k):
    """
        Do affine cipher encryption.
        compute ci ≡ ami + b (mod 26)

    :param str m: Plaintext. It consists of lowercase letter and space,comma ....
    :param tuple k: Key.  k = (a,b). Note that a and 26 must be coprime
    :return str c:
    """
    a = k[0]
    b = k[1]
    assert 0 < a < 26
    assert 0 <= b < 26
    assert gcd(a, 26) == 1

    c = ""
    for i in range(len(m)):
        if m[i].isalpha():
            c[i] = chr((a * (ord(m[i]) - 97) + b) % 26 + 97)
        else: # if m[i] is a space or sthg
            c[i] = m[i]

    return m

def affine_dec(c, *k):
    """
        ci ≡ ami + b (mod 26)  =>
        mi ≡ a^(-1) * (ci-b) (mod 26)

    :param str c: Ciphertext.
    :param tuple k: Same as above
    :return str m:
    """
    a = k[0]
    b = k[1]
    assert 0 < a < 26
    assert 0 <= b < 26
    assert gcd(a, 26) == 1

    m = ""
    for i in range(len(c)):
        if c[i].isalpha():
            m[i] = chr(invert(a) * (ord(c[i]) - 97 - b) % 26 + 97)
        else: # if m[i] is a space or sthg
            m[i] = c[i]

    return m

# TODO: Attack on affine cipher
'''
Consider that affine cipher is just a simple substitution cipher
So, why not use the website: https://quipqiup.com/  
'''

# -----------------------  Vigenere cipher

def Vigenere_enc(k,m):
    """
        example: k = "cafe"
                 m = "tellhimaboutme
                tell hima bout me
                cafe cafe cafe ca
           c =  VEQP JIRE DOZX OE

    :param str k: Key.
    :param str m: Plaintext.
    :return str c: Ciphertext.
    """
    c = ""

    key_len = len(k)
    key = [ord(k[i]) - 97 for i in range(key_len)]  # eg: if k = "cafe" then key = [2,0,5,4]
    for i in range(len(m)):
        c += chr(ord(m[i]) - 97 + key[i % key_len] % 26 + 97)

    return c

def Vigenere_dec(k, c):
    """

    :param str k: Key
    :param str c: Ciphertext
    :return str m: Plaintext
    """
    m = ""

    key_len = len(k)
    key = [ord(k[i]) - 97 for i in range(key_len)]  # eg: if k = "cafe" then key = [2,0,5,4]
    for i in range(len(c)):
        m += chr(ord(c[i]) - 97 - key[i % key_len] % 26 + 97)

    return m

# TODO: Attack on Vigenere cipher
'''
Just use this website: https://www.guballa.de/vigenere-solver
'''

# -----------------------  TODO: Hill cipher


















