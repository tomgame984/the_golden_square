from lib.code_02_cipher import *


def test_encode():
    encoded = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert encoded == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_decode():
    decorded = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert decorded == 'theswiftfoxjumpedoverthelazydog'