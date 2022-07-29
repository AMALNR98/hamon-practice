def panagram(s):
    s1 = s
    s1.lower()
    s1 = list(set(s1))
    alphabet = list(set("abcdefghijklmnopqrstuvwxyz"))
    count = 0
    i = 0
    while i < len(s1):
        if s1[i] in alphabet:
            count += 1
        i += 1
    if count == 26:
        print("Is panagram")
        return True
    print("Is not panagram")
    return False
s = "The quick brown fox jumps over the lazy dog"
panagram(s)