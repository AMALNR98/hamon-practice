import pytest
from panagram import panagram
from problems import palindrome,prime,freq


def test_paliendrome():
    assert palindrome("english") is False
    assert palindrome("a")is True
    assert palindrome("fox")is False
    assert palindrome("malayalam")is True
    assert palindrome("101")is True

def test_prime():
    assert prime("2")is True
    assert prime("4")is False
    assert prime("99") is False
    assert prime(11) is True
    assert prime(4)is False
    assert prime(9)is False

def test_freq():
    s ="amal"
    test_fre = {'a':2,
                'm':1,
                'l':1}
    assert freq(s)==test_fre

    s ="malayalam"
    malayalam = {'m':2,
                 'a':4,
                 'l':2,
                 'y':1}
    assert freq(s) == malayalam

def test_panagram():
    assert panagram("The quick brown fox jumps over the lazy dog") is True
    assert panagram("The quick brown fox jumped over the lazy dog") is False