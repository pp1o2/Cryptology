# coding=utf-8
import os

# -----------------------  shift cipher

def shift_enc(k, m):
    """
        Do shift cipher encryption.
        Calculate ci: ci ≡ mi+k (mod 26)

    :param int k: key of encryption. (0<k<26)
    :param str m: plaintext. All characters should be alphabetic.
    :return str c: ciphertext.
    """

    assert m.isalpha()
    assert 0 < k < 26

    c = ""
    for mi in m:
        if mi.islower():
            c += chr((ord(mi) - 97 + k) % 26 + 97)
        else:  # if mi is uppercase
            c += chr((ord(mi) - 65 + k) % 26 + 65)

    return c

def shift_dec(k,c):
    """
        Do shift cipher decryption.
        Calculate mi ≡ ci-k (mod 26)

    :param int k: key of decryption. (0<k<26)
    :param str c: ciphertext. All characters should be alphabetic.
    :return str m: plaintext.
    """

    assert c.isalpha()
    assert 0 < k < 26

    m = ""
    for ci in c:
        if ci.islower():
            m += chr((ord(ci) - 97 - k) % 26 + 97)
        else:
            m += chr((ord(ci) - 65 - k) % 26 + 65)

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
        os.system("cls")
        k = (k + 1) % 26

# TODO: shift_break_by_frequency_analysis(c)

'''
Just use this website for frequency analysis: https://quipqiup.com/ 
It can solve simple substitution ciphers.
'''

# TODO: Substitution cipher

def vigenere_enc(k,m):
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

def vigenere_dec(k,c):
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

# TODO: Attack on vigenere cipher
'''
Just use this website: https://www.guballa.de/vigenere-solver
'''

# TODO: Hill cipher
















