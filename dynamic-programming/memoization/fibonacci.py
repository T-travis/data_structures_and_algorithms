# https://en.wikipedia.org/wiki/Fibonacci_number
# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Time Complexity O(2^n): each function call makes two recursive function calls n times.
# thus the fib(n) function is making O(2^n-1) + O(2^n-2) + O(1) = O(2^n)
# Space Complexity O(n): n number of function calls are made (pushed to stack) and removed 
# (popped from stack) for each return thus never going above n.
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


#print(fib(5))   # 5
#print(fib(7))   # 13
#print(fib(50))  # 12586269025 this is slow!


# Time Complextity O(n): although each function call makes two recursive calls here, we don't
# make repeated calls to f(n) which cuts our tree down to a more linear structure
# Space Complexity: O(n)
def fib_memoization(n, mem):
    # keys represent n in fib(n) and values represent x in fib(n) = x

    # if n has been calculated, return the value/result
    if n in mem.keys(): return mem[n]

    # fib(n) where n <= 2 = 1, fin([0,1,2]) = 1
    if n <= 2: return 1

    # store the key/value pair
    mem[n] = fib_memoization(n-1, mem) + fib_memoization(n-2, mem)

    return mem[n]


#print(fib_memoization(0, {}))   # 5
print(fib_memoization(5, {}))   # 5
#print(fib_memoization(7, {}))   # 13
#print(fib_memoization(50, {}))  # 12586269025 this is fast!
