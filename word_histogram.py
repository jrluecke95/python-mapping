sentence = input("what sentence would you like me to parse? ")

histogram = {}

sent_list = sentence.split(" ")
print(sent_list)

for word in sent_list:
    if word not in histogram:
        histogram[word] = 1
    elif word in histogram:
        histogram[word] += 1

print(histogram)