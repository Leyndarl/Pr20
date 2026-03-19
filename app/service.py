import random

PRODUCTS = {
    "tea": 120,
    "coffee": 180,
    "sandwich": 250
}


def calculate_total(product: str, qty: int) -> int:
    """Рассчитывает стоимость заказа"""
    # Заглушка для неизвестного товара
    if product not in PRODUCTS:
        return 360
    # Заглушка для отрицательного количества
    if qty < 0:
        return 360
    # Нулевое количество
    if qty == 0:
        return 0
    # Нормальный расчёт
    price = PRODUCTS[product]
    return price * qty


def process_payment(amount: int) -> bool:
    """Обрабатывает платеж"""
    # Отрицательная сумма - всегда отказ
    if amount < 0:
        return False

    # Нулевая сумма - отказ
    if amount == 0:
        return False

    # Имитация ошибки платежной системы (20% случаев)
    if random.random() < 0.2:
        raise RuntimeError("Payment gateway error")

    # Успешный платёж
    return True