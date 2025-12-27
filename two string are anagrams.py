s="tae"
r="ate"
def anagram(s,r):
    if len(s)!=len(r):
        for char in s:
            if char not in r:
                return "Not anagram"
        return"anagram"
print(anagram(s,r))
