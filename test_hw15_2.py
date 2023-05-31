

from hw15_2 import sort_data


def test_sort_data_list():
    give_data = [2, 3, 4, 5, 6, 0]
    expected_data = (0, 2, 3, 4, 5, 6)
    assert sort_data(sequence=give_data) == expected_data


def test_sort_data_string():
    give_data = "cba"
    expected_data = ('a', 'b', 'c')
    assert sort_data(sequence=give_data) == expected_data


def test_sort_data_set():
    give_data = {'c', 'b', 'a'}
    expected_data = ('a', 'b', 'c')
    assert sort_data(sequence=give_data) == expected_data


def test_sort_data_dict():
    give_data = {5: 'TutorialsPoint', 7: 'Codes', 6: 'Python'}
    expected_data = 5, 6, 7
    assert sort_data(sequence=give_data) == expected_data
