import hello
def test_add():
    assert hello.add(3,8)==11
    assert hello.add(6)==8

def test_mul():
    assert hello.mul(6)==18
def test_add_strings():
    result= hello.add('hello ', 'world')
    assert result== 'hello world'
    assert type(result) is str
    assert 'hello' in result
def test_mul_strings():
    assert hello.mul('hello ',5)  == 'hello hello hello hello hello'
    result= hello.mul('hello ')
    assert result== 'hello hello hello'

