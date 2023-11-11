def find_hcf(x, y): #Euclidean algorithm to be used in this ques
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return abs(x * y) // find_hcf(x, y)

# Example usage
num1 = 12
num2 = 18

hcf_result = find_hcf(num1, num2)
lcm_result = find_lcm(num1, num2)

print(f"HCF of {num1} and {num2} is: {hcf_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")
