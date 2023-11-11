def fibonnaci_usingz_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonnaci_usingz_recursion(n-1) + fibonnaci_usingz_recursion(n-2)

# Example usage:
num_terms = 10
for i in range(num_terms):
    print(fibonnaci_usingz_recursion(i))
