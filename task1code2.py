#There's a potential issue in the get_age() function. The input() function returns a string, so when comparing age with the integer 18, it might raise an error. Additionally, the isnumeric() method checks if all characters in the string are numeric, but it doesn't handle negative numbers or floating-point values. Here's the corrected code:
# Changes made:Renamed the variable from age to age_str to make it clear that it's a string.
# Used isdigit() to check if the input string consists of digits.
# Checked age is not None instead of just age.
# These changes ensure that the input is a valid positive integer before attempting to convert it to an integer and compare it with 18.
def get_age():
    age_str = input("Please enter your age: ")
    if age_str.isdigit() and int(age_str) >= 18:
        return int(age_str)
    else:
        return None

def main():
    age = get_age()
    if age is not None:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
