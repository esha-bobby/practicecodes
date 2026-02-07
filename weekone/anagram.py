def are_anagrams(s, t):
    if len(s) != len(t):
        print("not an anagram")
        return

    for char in s:
        if s.count(char) != t.count(char):
            print("not an anagram")
            return

    print("yes an anagram")
are_anagrams('silent','listen')