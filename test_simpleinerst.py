from simpleinterst import simple_interst

def test_SI():
    assert simple_interst(2000,6,10) == 1200 

def test_SIzero():
    assert simple_interst(10000,0,0) == 0 