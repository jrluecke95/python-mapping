string = input("what word(s) would you like me to count for you today?")

word_count = {}

for letter in string:
    if letter not in word_count:
        word_count[letter] = 1
    elif letter in word_count:
        word_count[letter] += 1

print(word_count)    


