def remove_letter(sentence, letter):
    if letter not in sentence:
        return "Letter not found"
    return sentence.replace(letter, "")

text = input("Enter a sentence: ")
ch = input("Enter letter to remove: ")
print(remove_letter(text, ch))
