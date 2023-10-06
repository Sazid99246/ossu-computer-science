from hello import hello

def test_hello():
    assert hello() == "hello, world"

def test_arguement():
    assert hello("Sazid") == "hello, Sazid"