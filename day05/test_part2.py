from part2 import Vents


def test_one():
    v = Vents()
    v.add(1, 1, 5, 5)
    assert v.get_cell(1, 1) == 1
    assert v.get_cell(2, 2) == 1
    assert v.get_cell(3, 3) == 1
    assert v.get_cell(4, 4) == 1
    assert v.get_cell(5, 5) == 1


def test_five():
    v = Vents()
    v.add(5, 5, 1, 1)
    assert v.get_cell(1, 1) == 1
    assert v.get_cell(2, 2) == 1
    assert v.get_cell(3, 3) == 1
    assert v.get_cell(4, 4) == 1
    assert v.get_cell(5, 5) == 1


def test_two():
    v = Vents()
    v.add(5, 1, 1, 5)
    assert v.get_cell(5, 1) == 1
    assert v.get_cell(4, 2) == 1
    assert v.get_cell(3, 3) == 1
    assert v.get_cell(2, 4) == 1
    assert v.get_cell(1, 5) == 1


def test_three():
    v = Vents()
    v.add(1, 5, 5, 1)
    assert v.get_cell(5, 1) == 1
    assert v.get_cell(4, 2) == 1
    assert v.get_cell(3, 3) == 1
    assert v.get_cell(2, 4) == 1
    assert v.get_cell(1, 5) == 1
