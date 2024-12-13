def f(sentence: str) -> str:
    """
    Returns the sentence with spaces removed.

    Args:
        sentence (str): The sentence from which to remove spaces.

    Returns:
        str: The sentence without spaces.
    """
    return sentence.replace(" ", "")

print(f("integrated development environment"))
# Expected output: "integrateddevelopmentenvironment"

print(f("A programming language is a system of notation for writing computer programs"))
# Expected output: "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
