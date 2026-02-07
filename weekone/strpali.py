#check if s string is palindrome 
def palindrome(word):
    reversed=word[::-1]
    if reversed==word:
        print("is palindrome")
    else:
        print("not palindrome")
palindrome('malayalam')

def is_palindrome(word):
    reversed_str=''
    for ch in word:
        reversed_str=ch+reversed_str
    if reversed_str==word:
        print("is a palindrome")
    else:
        print("not a palindrome")
is_palindrome('hannah')


