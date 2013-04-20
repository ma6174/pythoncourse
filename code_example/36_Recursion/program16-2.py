def factorial(n):
    """Recursive factorial."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
