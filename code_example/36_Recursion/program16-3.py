def fibonacci(n):
    """Recursive Fibonacci sequence."""
    if n == 0 or n == 1:     # base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive case
