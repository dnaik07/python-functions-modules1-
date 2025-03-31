def factorial(n):
    """
    Calculate factorial of a number using iteration
    Args:
        n (int): Positive integer
    Returns:
        int: Factorial of n
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        print(f"\nFactorial of {num} is: {factorial(num)}")
    except ValueError:
        print("Error: Please enter a valid integer!")