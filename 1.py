def is_armstrong(n):
    s = str(n)
    total = sum(int(d)**len(s) for d in s)
    return 1 if total == n else 0

num = int(input("Enter a number: "))
print(is_armstrong(num))
