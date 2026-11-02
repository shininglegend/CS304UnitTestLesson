def shipping_cost(weight_lb):
    if weight_lb <= 0:
        raise ValueError("weight must be positive")
    if weight_lb < 1:
        return 5.00
    if weight_lb <= 5:
        return 9.00
    return 9.00 + 2.00 * int(weight_lb - 5)
