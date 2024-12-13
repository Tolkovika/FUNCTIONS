def f(amount_to_pay: int) -> int:
    """
    Calculates the minimum number of coins needed to pay a given amount.

    Args:
        amount_to_pay (int): The total amount to pay (in PLN).

    Returns:
        int: The minimum number of coins needed.
    """
    if amount_to_pay < 0:
        raise ValueError("Amount to pay must be a non-negative integer.")

    # Coins available in descending order
    coins = [5, 2, 1]
    num_coins = 0

    # Calculate the minimum number of coins
    for coin in coins:
        num_coins += amount_to_pay // coin  # Use as many coins of this denomination as possible
        amount_to_pay %= coin  # Update the remaining amount to pay

    return num_coins

# Test cases
print(f(23))  # Expected output: 6 (4×5 PLN, 1×2 PLN, 1×1 PLN)
print(f(8))   # Expected output: 3 (1×5 PLN, 1×2 PLN, 1×1 PLN)
print(f(2))   # Expected output: 1 (1×2 PLN)
print(f(0))   # Expected output: 0 (no coins needed)
