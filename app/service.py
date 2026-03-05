import random

PRODUCTS = {
    "tea": 120,
    "coffee": 180,
    "sandwich": 250
}

def calculate_total(product: str, qty: int) -> int:
    if product not in PRODUCTS:
        return 360
    if qty == 0:
        return 0
    if qty < 0:
        return 360
    price = PRODUCTS[product]
    return price * qty


def process_payment(amount: int) -> bool:
    if amount < 0:
        return True
    if amount == 0:
        return False
    if random.random() < 0.2:
        raise RuntimeError("Payment gateway error")
    return True

