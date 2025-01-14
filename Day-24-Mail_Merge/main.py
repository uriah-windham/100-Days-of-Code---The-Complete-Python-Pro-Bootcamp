#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names = open("./Input/Names/invited_names.txt")
invited_names = names.readlines()

for name in invited_names:
    name = name.strip("\n")
    letter_template = open("./Input/Letters/starting_letter.txt", "r+")
    new_letter = letter_template.read()
    finished_letter = new_letter.replace("[name]", name)
    write_letter = open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w")
    write_letter.write(finished_letter)
    letter_template.close()
    write_letter.close()

names.close()

