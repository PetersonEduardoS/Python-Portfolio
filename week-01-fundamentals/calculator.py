print("Simple Calculator")

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

operation = input("Enter the operation number: ")

if operation == "1":
    result = number_1 + number_2
    print("Result:", result)

elif operation == "2":
    result = number_1 - number_2
    print("Result:", result)

elif operation == "3":
    result = number_1 * number_2
    print("Result:", result)

elif operation == "4":
    if number_2 != 0:
        result = number_1 / number_2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation.")