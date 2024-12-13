def f(dice: str) -> int:
    # Initialize variables for the current streak and the maximum streak
    max_streak = 1
    current_streak = 1

    # Loop through the dice rolls starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            # If the current digit is the same as the previous one, increase the streak
            current_streak += 1
        else:
            # If the streak is broken, reset the current streak
            current_streak = 1

        # Update the maximum streak if the current streak is greater
        max_streak = max(max_streak, current_streak)

    return max_streak

print(f("5233165554211"))  # Expected output: 5
print(f("2133"))  # Expected output: 3
