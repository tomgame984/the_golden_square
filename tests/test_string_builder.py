from lib.string_builder import *

def test_I_string_builder_output_string():
    string = StringBuilder()
    string.add('Tom')
    assert string.output() == 'Tom'

def test_II_string_builder_output_str_len():
    string = StringBuilder()
    string.add('Tom')
    assert string.size() == 3

def test_III_adding_multiple_strings_outputs_concatenated_str():
    string = StringBuilder()
    string.add('Tom')
    string.add(' ')
    string.add('is')
    string.add(' ')
    string.add('a')
    string.add(' ')
    string.add('test')
    string.add(' ')
    string.add('wizard!')
    assert string.output() == 'Tom is a test wizard!'

def test_IV_adding_multiple_strings_outputs_str_len():
    string = StringBuilder()
    string.add('Tom')
    string.add(' ')
    string.add('is')
    string.add(' ')
    string.add('a')
    string.add(' ')
    string.add('test')
    string.add(' ')
    string.add('wizard!')
    assert string.size() == 21