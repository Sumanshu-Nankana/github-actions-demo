from src import  app


def test_addition_with_two_numbers():
    result = app.addition(10, 5)
    assert result == 15


def test_addition_with_negative_numbers():
    result = app.addition(-10, -5, -7)
    assert result == -22


def test_addition_with_single_number():
    result = app.addition(25)
    assert result == 25

def test_addition_with_zero_number():
    result = app.addition()
    assert result == 0