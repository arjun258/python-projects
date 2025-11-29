def lenWords(s):
    words = s.split()
    return tuple((len(w)) for w in words)

text = input("Enter a string: ")
print(lenWords(text.strip()))
