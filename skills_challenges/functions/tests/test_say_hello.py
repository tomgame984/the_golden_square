from lib.say_hello import *

# Intended output:
#
# > say_hello("kay")
# => "hello kay"

def test_name_output():
    assert say_hello("kay") == "hello kay"

def test_encode():
    encoded = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert encoded == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_decode():
    decorded = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert decorded == 'theswiftfoxjumpedoverthelazydog'