def total(price: float, qty: int, discount: float = 0.0) -> float:
    """Total do pedido com desconto percentual (0 a 1)."""
    if qty < 0 or not 0.0 <= discount <= 1.0:
        raise ValueError("quantidade ou desconto invalido")
    return round(price * qty * (1 - discount), 2)
