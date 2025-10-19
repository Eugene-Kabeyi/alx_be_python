class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition of two numbers.
        It does NOT access or modify class attributes or methods.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Performs multiplication and
        references a class attribute (calculation_type).
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
