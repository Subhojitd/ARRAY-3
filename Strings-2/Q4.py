def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

s = "I love to code"
print(reverseWords(s))