L = eval(input("Enter list L: "))
M = eval(input("Enter list M: "))

if len(L) == len(M):
    N = [L[i] + M[i] for i in range(len(L))]
    print(N)
else:
    print("Lists are not of same length")
