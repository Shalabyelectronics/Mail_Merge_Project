# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    contents = names.read()
    list_names = list(contents.split("\n"))

starting_letter = open("Input/Letters/starting_letter.txt")
letter_content = starting_letter.read()
for name in list_names:
    with open(f"Output/ReadyToSend/invite_{name}.txt", mode="w") as invited_letter:
        invited_letter.write(letter_content.replace("[name]", f"{name}"))
print(list_names)
starting_letter.close()
