from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5
def test_add2():
    assert 1 + 1 == 3 #error