import pytest
from app.pricing import total


def test_total_sem_desconto():
    assert total(10.0, 3) == 30.0


def test_total_com_desconto():
    assert total(10.0, 3, 0.1) == 27.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        total(10.0, 1, 1.5)
