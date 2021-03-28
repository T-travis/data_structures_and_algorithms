# https://en.wikipedia.org/wiki/Fibonacci_number
# 0, 1, 1, 2, 3, 5, 8, 13, ...


# Time O(n)
# Space O(n)
def fib(n):

    if n == 0: return 0

    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(n-1):
        fib_table[i+1] += fib_table[i]
        fib_table[i+2] += fib_table[i]
    
    fib_table[-1] += fib_table[-2]
    return fib_table[n]

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(50))
