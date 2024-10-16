class ArithmeticOperators:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

    def modulus(self, a, b):
        return a % b

    def exponent(self, a, b):
        return a ** b

    def floor_divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a // b

# Example usage
arith = ArithmeticOperators()
print("Add: ", arith.add(10, 5))
print("Subtract: ", arith.subtract(10, 5))
print("Multiply: ", arith.multiply(10, 5))
print("Divide: ", arith.divide(10, 5))
print("Modulus: ", arith.modulus(10, 5))
print("Exponent: ", arith.exponent(2, 3))
print("Floor Divide: ", arith.floor_divide(10, 3))
