

def add(*args):
    return sum(args)


def test_add():
    result = add(1, 2)
    assert result == 3, 'Function add must return 3'
    assert result > 0, 'Function add must return 3'


