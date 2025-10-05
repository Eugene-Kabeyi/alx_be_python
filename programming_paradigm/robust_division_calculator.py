def safe_divide(numerator, denominator):
    """Safely divides two numbers with error handling for invalid input and zero division."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric inputs
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."
