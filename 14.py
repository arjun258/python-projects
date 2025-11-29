def count_me_my():
    with open("story.txt", "r") as f:
        text = f.read()

    # Normalize
    text = text.lower()

    # Replace punctuation with spaces
    for p in ",.!?;:-":
        text = text.replace(p, " ")

    words = text.split()

    count = 0
    for w in words:
        if w == "me" or w == "my":
            count += 1

    print("Count of Me/My in file:", count)


count_me_my()
