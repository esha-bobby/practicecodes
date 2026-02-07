def min_window(s, t):
    if not t:
        return ""
    t_count = {}
    for ch in t:
        if ch in t_count:
            t_count[ch] += 1
        else:
            t_count[ch] = 1
    left = 0
    result = ""
    count = 0
    window = {}

    for right in range(len(s)):
        ch = s[right]
        if ch in window:
            window[ch] += 1
        else:
            window[ch] = 1

        if ch in t_count and window[ch] <= t_count[ch]:
            count += 1

        while count == len(t):
            current = s[left:right + 1]

            if result == "" or len(current) < len(result):
                result = current

            left_char = s[left]
            window[left_char] -= 1

            if left_char in t_count and window[left_char] < t_count[left_char]:
                count -= 1

            left += 1

    return result
