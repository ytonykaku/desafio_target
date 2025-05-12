import sys

def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reverse_string.py <string_to_reverse>")
    else:
        user_input = sys.argv[1]
        reversed_result = reverse_string(user_input)
        print(f"Reversed string: {reversed_result}")
