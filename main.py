from src.longest_substring import longest_unique_substring
from src.circular_binary import has_four_consecutive_ones_circular


def main():
    print("=== Algorithm Challenge ===")
    print("1. Longest Unique Substring")
    print("2. Circular Binary")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        user_input = input("Enter a string: ")
        result = longest_unique_substring(user_input)
        print(f"Result: {result}")

    elif choice == "2":
        user_input = input("Enter a binary string: ")
        result = has_four_consecutive_ones_circular(user_input)
        print(f"Result: {result}")

    elif choice == "0":
        pass

    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()
