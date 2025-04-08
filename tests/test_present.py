import pytest
from lib.present import *

# Check wrap
def test_wrap_Present():
    present = Present()
    present.wrap("Gift")
    assert present.contents == "Gift"
# Check re-wrap blocker
    with pytest.raises(Exception) as not_pass_the_parcel:
        present.wrap("Another layer of paper")
    assert str(not_pass_the_parcel.value) == "A contents has already been wrapped."

# Check unwrap
def test_unwrap_Present():
    present = Present()
    present.wrap("Gift")
    assert present.unwrap() == "Gift"
# Check can't remove no wrapping
    unwrapped = Present()
    with pytest.raises(Exception) as not_wrapped:
        unwrapped.unwrap()
    assert str(not_wrapped.value) == "No contents have been wrapped."