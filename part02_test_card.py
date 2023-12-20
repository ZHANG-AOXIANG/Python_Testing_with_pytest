# Date:2023-12-20
# Author:Aoxiang Zhang
# Purpose:Learn Pytest from "Python Testing with pytest" by Brian Okken. Today, I am learning for "PartI.Primary power - 2.Writing Test Functions

from cards import Card

"""
Card Data Structure
Card{
    id: XXX
    state: XXX
    owner: XXX
    summary: XXX
}
"""


# test for default Card
def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


# test to access the card field
def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123


# test for the same two cards
def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)
    assert c1 == c2


# test for the two cards with different ids
# If they are just different ids, the two cards are same.
def test_equality_with_diff_ids():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 456)
    # assert c1.id != c2.id
    assert c1 == c2


# test for the two cards with different state
def test_equality_with_diff_state():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "done", 123)
    assert c1 != c2


# test for the two cards with different owner
def test_equality_with_diff_owner():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "Jack", "todo", 123)
    assert c1 != c2


# test for the two cards with different summary
def test_equality_with_diff_summary():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("thing1", "brian", "todo", 123)
    assert c1 != c2


# test for two completely different cards
def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert c1 != c2


# test from_dict() function
def test_from_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2_dict = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


# test to_dict() function
def test_to_dict():
    c1 = Card("something", "brian", "todo", 123)
    c1_dict = c1.to_dict()
    c1_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123
    }
    assert c1_dict == c1_expected
