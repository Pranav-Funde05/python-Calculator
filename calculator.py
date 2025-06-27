import math

def add_numbers():
    print("Let's add two numbers!")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x + y

def subtract_numbers():
    print("Let's subtract two numbers!")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x - y

def multiply_numbers():
    print("Let's multiply two numbers!")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x * y

def divide_numbers():
    print("Let's divide two numbers!")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if y == 0:
        return "❌ Cannot divide by zero!"
    return x / y

def square_root():
    print("Let's find square root of a number!")
    z = int(input("Enter the number you want to find the square root of: "))
    result = math.sqrt(z)
    return result

def cube_root():
    print("Lets find cube root of a number!")
    z = int(input("Enter the number you want to find the cube root of: "))
    result = math.pow(z, 1/3)
    return result


print("=====================================================================================================================")
print("🙋 Hello User!!!")
print("Welcome to the calculator 🧮")
print("=====================================================================================================================")
while True:
    print("The functions you can perform here are:")
    print(" 1. Add Numbers\n 2. Subtract Numbers\n 3. Multiply Numbers\n 4. Divide Numbers\n 5. Find square root of a number\n " \
          "6. Find cube root of a number")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

    selection = int(input("Enter the respective number of the function you wish to perform: "))

    if selection == 1:
        print("✅ The sum of these two numbers is:", add_numbers())
    elif selection == 2:
        print("✅ The result after subtracting second number from first is:", subtract_numbers())
    elif selection == 3:
        print("✅ The product(multiplication) of these two numbers is:", multiply_numbers())
    elif selection == 4:
        print("✅ The quotient after dividing these two numbers is:", divide_numbers())
    elif selection == 5:
        print("✅ Square root of the number is", square_root())
    elif selection == 6:
        print("✅ Cube root of the number is", cube_root())
    else:
        print("Wrong Input")

    print("=====================================================================================================================")
    again = input("🔁 Want to perform another calculation? (yes/no): ").lower()
    if again != "yes":
     print("=====================================================================================================================")
     print("Thanks for using the calculator 🙏")
     print("=====================================================================================================================")
     break
    