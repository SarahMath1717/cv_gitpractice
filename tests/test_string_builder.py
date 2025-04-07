from lib.string_builder import *

#test that 0 input is also 0 output
def test_StringBuilder():
    string = StringBuilder()
    assert string.output() == ""

#start adding to string
def test_StringBuilder_with_input():
    string = StringBuilder()
    string.add("Where")
    assert string.output() == "Where"
    string.add(" are")
    assert string.output() == "Where are"
    string.add(" my socks?")
    assert string.output() == "Where are my socks?"

#check the math
def test_StringBuilder_length_check():
    string = StringBuilder()
    assert string.size() == 0
    string.add("Chips")
    assert string.size() == 5
    string.add(" and beans")
    assert string.size() == 15