def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

#The code provided appears to be correct, and it should work as intended. However, there is a potential issue with the variable name "reversed" because it is also the name of a built-in function in Python. While it won't cause any immediate errors in this code, it's a good practice to avoid using names that are already used by Python built-in functions to prevent confusion and potential bugs in the future.
#Therefore, I changed the variable name from "reversed" to "reversed_str" to avoid potential naming conflicts.
