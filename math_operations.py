import math

def calculate_operations(number):
    """
    Perform mathematical operations using math module
    Args:
        number (float): Input number
    Returns:
        dict: Dictionary of calculated results
    """
    return {
        "square_root": math.sqrt(number),
        "natural_log": math.log(number),
        "sine": math.sin(number)
    }

if __name__ == "__main__":
    print("MATH MODULE OPERATIONS")
    print("----------------------")
    
    try:
        num = float(input("Enter a number: "))
        results = calculate_operations(num)
        
        print(f"\nResults for {num}:")
        print(f"Square root: {results['square_root']:.4f}")
        print(f"Natural logarithm: {results['natural_log']:.4f}")
        print(f"Sine (radians): {results['sine']:.4f}")
    except ValueError:
        print("Error: Please enter a valid number!")
    except Exception as e:
        print(f"Error: {str(e)}")