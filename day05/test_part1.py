from part1 import Vents


def test_one():
    v = Vents()
    v.add(1, 1, 1, 2)
    assert v.get_cell(1, 1) == 1
    assert v.get_cell(1, 2) == 1


def test_two():
    v = Vents()
    v.add(1, 1, 1, 5)
    assert v.get_cell(1, 1) == 1
    assert v.get_cell(1, 2) == 1
    assert v.get_cell(1, 5) == 1


def test_three():
    v = Vents()
    v.add(1, 5, 1, 1)
    assert v.get_cell(1, 1) == 1
    assert v.get_cell(1, 5) == 1


def test_four():
    v = Vents()
    v.add(1, 5, 3, 5)
    assert v.get_cell(1, 5) == 1
    assert v.get_cell(2, 5) == 1
    assert v.get_cell(3, 5) == 1
