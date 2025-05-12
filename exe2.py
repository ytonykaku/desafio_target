import math
import argparse

def is_perfect_square(x: int) -> bool:
    root = math.isqrt(x)
    return root * root == x

def is_fibonacci_number(n: int) -> bool:
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def main():
    parser = argparse.ArgumentParser(description="Check if a number is part of the Fibonacci sequence.")
    parser.add_argument("number", type=int, help="The number to check")

    args = parser.parse_args()
    number = args.number

    if number < 0:
        print("Negative numbers are not part of the Fibonacci sequence.")
    elif is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is not a Fibonacci number.")

if __name__ == "__main__":
    main()
