def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def run_calculator():
    print(" Production-Ready Calculator ")
    
    while True:
        print("\nAvailable Operations:")
        print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '5':
            print("Shutting down calculator. Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select a number from 1 to 5.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    run_calculator()
