import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.service import calculate_total, process_payment


def test_calculate_total_ok():
    assert calculate_total("coffee", 2) == 360


def test_calculate_total_zero():
    assert calculate_total("tea", 0) == 0


def test_unknown_product():
    result = calculate_total("unknown_product", 2)
    assert result == 360


def test_negative_quantity():
    result = calculate_total("coffee", -2)
    assert result == 360


def test_process_payment_negative_amount():
    result = process_payment(-100)
    assert result is False


def test_process_payment_zero():
    result = process_payment(0)
    assert result is False


def test_process_payment_success():
    success = False
    for _ in range(10):
        try:
            result = process_payment(500)
            if result is True:
                success = True
                break
        except RuntimeError:
            continue
    assert success


def test_process_payment_random_failure():
    failures = 0
    attempts = 100

    for _ in range(attempts):
        try:
            result = process_payment(100)
            if result is False:
                failures += 1
        except RuntimeError:
            failures += 1

    error_rate = (failures / attempts) * 100
    print(f"\nПроцент ошибок: {error_rate:.1f}% ({failures}/{attempts})")

    assert 10 <= error_rate <= 30, f"Ожидалось ~20% ошибок, получено {error_rate:.1f}%"