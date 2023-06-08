def test_1():
    assert all_division(10) == 10


def test_2():
    assert all_division(10, 5) == 2


def test_3():
    assert all_division(10, 5, 2) == 1


def test_4():
    assert all_division(10, 5, 2, 2) == 0.5


def test_5():
    try:
        all_division(10, 5, 2, 2, 0)
    except ZeroDivisionError:
        assert True