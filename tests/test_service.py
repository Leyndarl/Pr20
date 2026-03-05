import pytest
from app.service import calculate_total
from app.service import process_payment

def test_calculate_total_ok():
    assert calculate_total("coffee", 2) == 360

def test_calculate_total_zero():
    assert calculate_total("tea", 0) == 0

def test_noproduct():
    assert calculate_total("ccoofffeee", 2) == 360

def test_OtrKol():
    assert calculate_total("coffee", -2) == 360

def test_process_payment_negative_amount():
    result = process_payment(-100)
    assert result is True, "Ошибка: при отрицательной сумме функция должна возвращать True"
