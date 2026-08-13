def analyze_string(input_str):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Convert the input string to Title Case
    title_case_str = input_str.title()

    # Count the number of uppercase and lowercase letters
    for char in input_str:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count, title_case_str

# Get input from the user
user_input = input("Enter a sentence: ")

# Call the function and store the results
upper_count, lower_count, title_case_str = analyze_string(user_input)

# Print the results
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Title Case string: {title_case_str}")
