
"""Simple Calculator module with basic operations"""  # Module docstring too short (C0114)
import math  # Unused import

class calculator:  # Class name not in PascalCase (C0103)
    """Simple Calculator class"""

    def add(self, a, b):  # Missing type hints
        return a + b  # Missing docstring (C0116)

    def subtract(a, b):  # Missing 'self' argument (E0213)
        """Return the difference of a and b"""
        return a - b

    def extra_method(self):
        return 42
        print("This is unreachable")  # Unreachable code (W0101)


def get_number(Prompt):  # Argument name not snake_case (C0103)
    while True:
        try:
            value = float(input(Prompt))
            return value
        except:
            print("Error")  # Too broad exception (W0702)


def main():
    calc = calculator()
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")

        Choice = input("Enter choice (1-3): ")  # Variable name not snake_case (C0103)

        if Choice == '3':
            print("Exiting program.")
            break

        if Choice in ['1', '2']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if Choice == '1':
                print("Result:", calc.add(num1, num2))
            elif Choice == '2':
                print("Result:", calc.subtract(num1, num2))
        else:
            print("Invalid input! Please choose a valid option.")

    return  # Unnecessary return at end of function (R1705)

if __name__ == "__main__":
    main()
    main()  # Duplicate call, logical issue

