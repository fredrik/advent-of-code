from d11 import valid_password


def test_valid_password():
    assert not valid_password("hijklmmn")
    assert not valid_password("abbceffg")
    assert not valid_password("abbcegjk")

    assert valid_password("ghjaabcc")
