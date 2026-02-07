def longest_unique_substring(s):
    longest = 0
    current = ""
    for ch in s:
        if ch in current:
            current = current[current.index(ch) + 1:]
        current += ch
        longest = max(longest, len(current))
    return longest

