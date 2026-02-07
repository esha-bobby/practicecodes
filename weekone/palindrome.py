
def is_palindrome(number):
    reverse=number[::-1]
    print(reverse)
    if number == reverse:
        print("is palindrome")
    else:
        print("not palindrome")

is_palindrome('232')

def palindrome(num):
    org=num
    reversed=0
    if num==0:
        print("invalid input")
    else:
        digit = num % 10
        reversed = (reversed * 10) + digit
        num //= 10
    return org == reversed

palindrome(67)

