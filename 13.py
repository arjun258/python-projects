with open("story.txt", "r") as f:
    text = f.read()

# lowercase everything
text = text.lower()

# replace punctuation with spaces
for p in ",.!?;:-":
    text = text.replace(p, " ")

words = text.strip().split()
total_words = len(words)

count_the = 0
for w in words:
    if w == "the":
        count_the += 1

print("Total words:", total_words)
print('Occurrences of "the":', count_the)
