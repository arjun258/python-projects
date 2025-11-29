a, b = 0, 1
fib = [a, b]

for _ in range(7):
    a, b = b, a + b
    fib.append(b)

fib_tuple = tuple(fib)
print(fib_tuple)
