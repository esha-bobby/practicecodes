def reverse(text):
    reversed_string=""
    for i in text:
        reversed_string=i+reversed_string
    return reversed_string
print(reverse('hello'))


def reversal(meow):
    return meow[::-1]

print(reversal('chocolate'))