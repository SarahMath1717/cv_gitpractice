from lib.gratitudes import *

#check formatting works
def test_format_Gratitudes():
    thankful_for = Gratitudes()
    result = thankful_for.format()
    assert result == "Be grateful for: "

#check adding 'tudes
def test_add_Gratitudes():
    thankful_for = Gratitudes()
    thankful_for.add("cheese")
    assert "cheese" in thankful_for.gratitudes

#combine both
def test_more_Gratitudes():
    thankful_for = Gratitudes()
    thankful_for.add("cheese")
    result = thankful_for.format()
    assert result == "Be grateful for: cheese"

#start list of gratitude
def test_lots_of_Gratitudes():
    thankful_for = Gratitudes()
    thankful_for.add("cheese")
    thankful_for.add("wine")
    thankful_for.add("deli meats")
    result = thankful_for.format()
    assert result == "Be grateful for: cheese, wine, deli meats"