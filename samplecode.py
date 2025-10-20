"""Simple Calculator module with basic operations"""


class Calculator:
    """Simple Calculator class"""

    def add(self, a, b):
        """Return the sum of a and b"""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b"""
        return a - b


def get_number(prompt):
    """Prompt the user for a number and validate input"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main program to interact with the Calculator"""
    calc = Calculator()
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == '3':
            print("Exiting program.")
            break

        if choice in ['1', '2']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
        else:
            print("Invalid input! Please choose a valid option.")


if __name__ == "__main__":
    main()

