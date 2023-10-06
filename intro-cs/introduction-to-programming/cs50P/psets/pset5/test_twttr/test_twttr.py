from twttr import shorten
import pytest

def test_shortener():
    shorten("twitter") == "twttr"
    assert shorten("this is my tweet!") == "ths s my twt!"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("s0meth1ng") == "s0mth1ng"