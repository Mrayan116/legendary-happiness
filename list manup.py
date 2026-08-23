# Task 1: Reverse a String.
def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str  # Build the reversed string character by characters
    return reversed_str

# Task 2: Count Vowels
def count_vowels(input_string):
    input_string = input_string.lower()  # Convert the input to lowercase for case-insensitivity
    count = 0
    vowels = "aeiou"  # Define a string containing vowels
    for char in input_string:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the count if it's a vowel
    return count

# Task 3: Remove Whitespace
def remove_whitespace(input_string):
    no_whitespace_str = ""
    for char in input_string:
        if char != ' ' and char != '\t':  # Check if the character is not a space or tab
            no_whitespace_str += char  # Build the result string without whitespace
    return no_whitespace_str

# Task 4: Word Count
def word_count(input_string):
    words = input_string.split()  # Split the input string into words based on spaces
    count = len(words)  # Count the number of words
    return count

# Task 5: Replace Substring
def replace_substring(input_string, substring, replacement):
    replaced_str = input_string.replace(substring, replacement)  # Replace the substring with the replacement
    return replaced_str

# Main loop for task selection
while True:
    print("Choose a task:")
    print("1. Reverse a String")
    print("2. Count Vowels")
    print("3. Remove Whitespace")
    print("4. Word Count")
    print("5. Replace Substring")
    print("Type 'exit' to quit.")
    
    choice = input("Enter the task number: ")
    
    if choice == 'exit':
        break  # Exit the loop if 'exit' is entered
    
    if choice not in ('1', '2', '3', '4', '5'):
        print("Invalid choice. Please enter a valid task number.")
        continue  # Continue to the next iteration of the loop
    
    input_string = input("Enter a string: ")  # Prompt the user for a string
    
    if choice == '1':
        print("Task 1: Reverse a String")
        result = reverse_string(input_string)  # Call the reverse_string function
    elif choice == '2':
        print("Task 2: Count Vowels")
        result = count_vowels(input_string)  # Call the count_vowels function
    elif choice == '3':
        print("Task 3: Remove Whitespace")
        result = remove_whitespace(input_string)  # Call the remove_whitespace function
    elif choice == '4':
        print("Task 4: Word Count")
        result = word_count(input_string)  # Call the word_count function
    elif choice == '5':
        substring = input("Enter the substring to replace: ")  # Prompt user for the substring
        replacement = input("Enter the replacement string: ")  # Prompt user for the replacement
        print("Task 5: Replace Substring")
        result = replace_substring(input_string, substring, replacement)  # Call the replace_substring function
    
    print("Output:", result)  # Display the result of the selected task
