def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def largest_palindrome_product(digits):
    max_value = 10**digits - 1
    min_value = 10**(digits - 1)
    max_palindrome = 0

    for i in range(max_value, min_value - 1, -1):
        for j in range(i, min_value - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break  # Further decreases in j will only result in smaller products
            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome

# Example usage:
num_digits = int(input("Enter the number of digits: "))
result = largest_palindrome_product(num_digits)
print(f"The largest palindrome product of {num_digits}-digit numbers is {result}")
