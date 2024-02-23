# Defining a base case
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Making a recursive call
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Handling recursive calls (tail recursion, memoization)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Analyzing the time complexity of a recursive algorithm
The time complexity of the fibonacci function is exponential, O(2^n), because each call to the function results in two additional calls.

# Analyzing the space complexity of a recursive algorithm
The space complexity of the fibonacci function is linear, O(n), because it requires memory for each function call on the call stack.
    
# Converting an iterative algorithm to a recursive algorithm
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Converting a recursive algorithm to an iterative algorithm
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
