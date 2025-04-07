from lib.counter import *

#test that 0 input is also 0 output
def test_Counter():
    counting = Counter()
    assert counting.count ==0

#using numbers
def test_Counter_with_input():
    counting = Counter()
    counting.add(2)
    assert counting.count == 2
    counting.add(7)
    assert counting.count == 9

#phrase it correctly
def test_report():
    counting = Counter()
    assert counting.report() == "Counted to 0 so far."
    counting.add(10)
    assert counting.report() == "Counted to 10 so far."