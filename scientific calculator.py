import os
from time import sleep

def clear_screen():
    os.system("cls")

def pause():
    print(
        "Calculating..."
    )
    sleep(1.5)

def back_to_menu():
    option = input(
        "\nDo you want to return to the main menu? (Y/N): "
    ).strip().lower()
    return option == 'y'

def addition():
    print(
        "\n-=-=-=- ADDITION CALCULATOR -=-=-=-\n"
    )
    total = 0
    while True:
        total += float(input(
            "Enter a number to add: "
        ))
        if input(
            "Do you want to add another number? (Y/N): "
        ).strip().lower() == 'n':
            break
    pause()
    print(
        f"\nThe result of the addition is: {total}\n"
    )

def subtraction():
    print(
        "\n-=-=- SUBTRACTION CALCULATOR -=-=-\n"
    )
    result = float(input(
        "Enter the first number: "
    ))
    while input(
        "Do you want to subtract another number? (Y/N): "
    ).strip().lower() == "y":
        result -= float(input(
            "Enter the number to subtract: "
        ))
    pause()
    print(
        f"\nThe result of the subtraction is: {result}\n"
    )

def multiplication():
    print(
        "\n-=-=- MULTIPLICATION CALCULATOR -=-=-\n"
    )
    result = float(input(
        "Enter the first number: "
    ))
    while input(
        "Do you want to multiply by another number? (Y/N): "
    ).strip().lower() == 'y':
        result *= float(input("Enter the next number: "))
    pause()
    print(
        f"\nThe result of the multiplication is: {result}\n"
    )

def division():
    print(
        "\n-=-=- DIVISION CALCULATOR -=-=-\n"
    )
    result = float(input(
        "Enter the first number: "
    ))
    while input(
        "Do you want to divide by another number? (Y/N): "
    ).strip().lower() == 'y':
        divisor = float(input(
            "Enter the divisor: "
        ))
        if divisor != 0:
            result /= divisor
        else:
            print(
                "Error: division by zero!"
            )
    pause()
    print(
        f"\nThe result of the division is: {result}\n"
    )

def exponentiation():
    print(
        "\n-=-=- EXPONENTIATION CALCULATOR -=-=-\n"
    )
    base = float(input(
        "Enter the base: "
    ))
    exponent = float(input(
        "Enter the exponent: "
    ))
    result = base ** exponent
    pause()
    print(
        f"The result of the exponentiation is: {result}"
    )

def multiplication_table():
    print(
        "\n-=-=- MULTIPLICATION TABLE -=-=-\n"
    )
    number = int(input(
        "Enter a number: "
    ))
    for i in range(1, 11):
        print(
            f"{number} x {i} = {number * i}"
        )

def calculate_percentage():
    print(
        "\n-=-=- PERCENTAGE CALCULATOR -=-=-\n"
    )
    print(
        "[1] - Simple percentage\n[2] - Discount\n[3] - Interest"
    )
    type_ = int(input(
        "Choose: "
    ))

    if type_ == 1:
        value = float(input(
            "Enter the value: "
        ))
        percentage = float(input(
            "Enter the percentage: "
        ))
        result = (percentage / 100) * value
        pause()
        print(
            f"{percentage}% of {value} is {result}"
        )

    elif type_ == 2:
        value = float(input(
            "Enter the product value: "
        ))
        rate = float(input(
            "Enter the rate (%): "
        )) / 100
        time = int(input(
            "Enter the time (months): "
        ))
        interest = value * rate * time
        total = value + interest
        pause()
        print(
            f"Interest: ${interest:.2f}, Total: ${total:.2f}"
        )

    elif type_ == 3:
        value = float(input(
            "Enter the original value: "
        ))
        rate = float(input(
            "Enter the discount rate (%): "
        )) / 100
        time = int(input(
            "Enter the time (months): "
        ))
        discount = value * rate * time
        final = value - discount
        pause()
        print(
            f"Discount: ${discount:.2f}, Value after discount: ${final:.2f}"
        )

def power():
    print(
        "\n-=-=- POWER CALCULATOR -=-=-\n"
    )
    base = float(input(
        "Enter the base: "
    ))
    exponent = float(input(
        "Enter the exponent: "
    ))
    result = base ** exponent
    pause()
    print(
        f"Result: {result}"
    )

def area():
    print(
        "\n-=-=- AREA CALCULATOR -=-=-\n"
    )
    print(
        "[1] Triangle\n[2] Square\n[3] Trapezoid\n[4] Circle\n[5] Rhombus"
    )
    option = int(input(
        "Choose: "
    ))

    if option == 1:
        base = float(input(
            "Base: "
        ))
        height = float(input(
            "Height: "
        ))
        print(
            f"Area of the triangle: {(base * height) / 2}"
        )

    elif option == 2:
        side = float(input(
            "Side of the square: "
        ))
        print(
            f"Area of the square: {side ** 2}"
        )

    elif option == 3:
        smaller_base = float(input(
            "Smaller base: "
        ))
        larger_base = float(input(
            "Larger base: "
        ))
        height = float(input(
            "Height: "
        ))
        print(
            f"Area of the trapezoid: {((larger_base + smaller_base) * height) / 2}"
        )

    elif option == 4:
        radius = float(input(
            "Radius: "
        ))
        print(
            f"Area of the circle: {3.14 * (radius ** 2):.2f}"
        )

    elif option == 5:
        smaller_diag = float(input(
            "Smaller diagonal: "
        ))
        larger_diag = float(input(
            "Larger diagonal: "
        ))
        print(
            f"Area of the rhombus: {(larger_diag * smaller_diag) / 2}"
        )

def root_calculation():
    print(
        "\n-=-=- ROOT CALCULATOR -=-=-\n"
    )
    number = float(input(
        "Enter the number: "
    ))
    index = float(input(
        "Enter the index (e.g., 2 for square root): "
    ))
    root = number ** (1 / index)
    pause()
    print(
        f"The {index} root of {number} is: {root}"
    )

while True:
    clear_screen()
    print(
        "\n===== SCIENTIFIC CALCULATOR ====="
    )
    print(
        "[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] Exponentiation\n[6] Multiplication Table\n[7] Percentage\n[8] Power\n[9] Area\n[10] Root\n[0] Exit"
    )

    try:
        choice = int(input(
            "Choose an option: "
        ))
        clear_screen()

        if choice == 0:
            break
        elif choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            exponentiation()
        elif choice == 6:
            multiplication_table()
        elif choice == 7:
            calculate_percentage()
        elif choice == 8:
            power()
        elif choice == 9:
            area()
        elif choice == 10:
            root_calculation()
        else:
            print(
                "Invalid option!"
            )

        if not back_to_menu():
            break

    except ValueError:
        print(
            "Please enter a valid option."
        )
        
