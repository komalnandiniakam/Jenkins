import calculator

assert calculator.add(2, 3) == 5
assert calculator.subtract(5, 3) == 2
assert calculator.multiply(2, 3) == 6
assert calculator.divide(6, 3) == 2
assert calculator.modulus(10, 3) == 1
assert calculator.modulus(10, 0) is None
print("All tests passed")
