from lib.code_01_say_hello import *

# Intended output:
#
# > say_hello("kay")
# => "hello kay"

def test_name_output():
    assert say_hello("kay") == "hello kay"
