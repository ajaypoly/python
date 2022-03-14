from postfix_program import postfix


def test_postfix_int():
    ret = postfix("23331+-*/")
    assert ret ==  1.5


def test_postfix_alpha():
    ret = postfix("abcd")
    assert ret ==  None


def test_postfix_alphanum():
    ret = postfix("123abc+-")
    assert ret ==  4

