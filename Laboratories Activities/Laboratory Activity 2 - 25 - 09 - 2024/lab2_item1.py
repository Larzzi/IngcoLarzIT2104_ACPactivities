def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

num = int(input("Enter an integer: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")
