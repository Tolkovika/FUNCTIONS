def f(detector: str) -> bool:
    """
    Returns True if at least 3 people were in the room at the same time, otherwise False.

    Args:
        detector (str): A string representing people entering ('+') and leaving ('-') the room.

    Returns:
        bool: True if at least 3 people were in the room at the same time, False otherwise.
    """
    count = 0
    for event in detector:
        if event == '+':
            count += 1
        elif event == '-':
            count -= 1

        # Check if at least 3 people are in the room at the same time
        if count >= 3:
            return True

    return False

# Test cases
print(f("+-+++-+---"))  # Expected output: True
print(f("+-+-+-+-"))    # Expected output: False
print(f("+-++-+--"))     # Expected output: False
print(f("+-++-++-+---")) # Expected output: True
