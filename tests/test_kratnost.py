from main import kratnost
import pytest

@pytest.mark.parametrize("a, b, expected_result",[([3, 9, 27, 33], 3, True),
                                                  ([2, 4, 6, 80], 2, True),
                                                  ([5, 25, 5, 90], 3, True)
                                                  ])
def test_kratnost(a, b, expected_result):
    assert kratnost(a, b) == expected_result

#здесь проиходит проверка 3 тестов для функции kratnost для елементов list