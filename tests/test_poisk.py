from main import poisk
import pytest

@pytest.mark.parametrize("a, b, expected_result",[({'masha':'+7976672...', 'misha':'+287672...', 'sasha':'havent phone'}, 'masha', True),
                                                  ({'dino':'dead', 'tiger':'alive', 'bird':'alive'}, 'bird', True),
                                                  ({'Jo':'math', 'Dina':'IT', 'Jim':'Chemistry'}, 'Dave', True)
                                                  ])
def test_poisk(a, b, expected_result):
    assert poisk(a, b) == expected_result

#здесь проиходит проверка 3 тестов для функции poisk в dict.