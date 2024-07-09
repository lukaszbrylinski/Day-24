#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
text = ""
with open("./Input/Letters/starting_letter.txt") as letter:
    base_letter = letter.readlines()
    for item in base_letter:
        text += item

with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    for name in list_of_names:
        new_name = name.strip()
        with open(f"./Output/ReadyToSend/{new_name}.txt", mode="w") as file:
            new_letter = text.replace("[name]", f"{new_name}")
            file.write(new_letter)
    print(type(list_of_names))
    print(list_of_names[0])


print(list_of_names)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp