def find_missing_number(num):
    n = len(num)

    for i in range(n + 1):
        if i not in num:
            return i
print(find_missing_number([3, 0, 1,])) 