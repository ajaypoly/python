from postfix_program import postfix


def test_postfix_int():
    ret = postfix("231+-")
    assert ret ==  2


def test_postfix_alpha():
    ret = postfix("abcd")
    assert ret ==  None
