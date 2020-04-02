from Classical_Crypto import *

def test_shift_enc():
    k = 7
    m = "SuiyuanQifei"
    print "%s" %shift_enc(k,m)

def test_shift_dec():
    k = 7
    m = "SuiyuanQifei"
    c = shift_enc(k,m)
    print "%s" %shift_dec(k,c)

def test_caesar_enc():
    m = "dCodeCaesar"
    print "%s" %caeser_enc(m)

def test_caesar_dec():

    m = "dCodeCaesar"
    c = caeser_enc(m)
    print "%s" %caeser_dec(c)

def test_shift_break_by_brute_force():
    c = "gFrghFdhvdu"
    shift_break_by_brute_force(c)

def test_shift_cipher():
    test_shift_enc()
    test_shift_dec()
    test_caesar_enc()
    test_caesar_dec()
    test_shift_break_by_brute_force()

if __name__ == '__main__':
    test_shift_cipher()