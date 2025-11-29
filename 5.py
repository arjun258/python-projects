nums = []
print("Enter 10 integers:")
for i in range(10):
    while True:
        try:
            n = int(input(f"{i+1} enter a number : "))
            nums.append(n)
            break
        except ValueError:
            print("Invalid input. Please enter an integer:")

print("Prime numbers are: ", end = "")
for n in nums:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(f"{n},", end = "")
