user_name = input("Welcome to Mad Libs! Please enter your name: ")

print(f"\nHello, {user_name}! Get ready to create a hilarious Mad Libs story together.")
print("You will be asked to provide words with specific parts of speech to fill in the blanks in our story.")
print("Let's start by entering some words!")

noun1 = input("Enter the first noun: ")
adjective1 = input("Enter the first adjective: ")
noun2 = input("Enter the second noun: ")
adjective2 = input("Enter the second adjective: ")
adverb = input("Enter an adverb: ")
adjective3 = input("Enter the third adjective: ")  
noun3 = input("Enter the third noun: ")  

story = f"\nGreat job, {user_name}! Once upon a time, there were two {adjective1} {noun1}s named Bob and Alice. "
story += f"They lived in a {adjective2} {noun2} and loved to {adverb} together.\n"
story += f"One day, they decided to go on an adventure, searching for a {adjective3} {noun3} treasure.\n"
story += f"{user_name} joined their quest, and together they found the treasure and lived happily ever after."

print("\nHere's your Mad Libs story:\n")
print(story)
