sentence = input("what sentence would you like me to parse? ")

histogram = {}

sent_list = sentence.split(" ")

for word in sent_list:
    if word not in histogram:
        histogram[word] = 1
    elif word in histogram:
        histogram[word] += 1

#print(histogram)

sorted_values = sorted(histogram.values())
sorted_values.sort(reverse=True)
sorted_dict= {}

for value in sorted_values:
    for word in histogram:
        if histogram[word] == value:
            sorted_dict[word] = histogram[word]

print("the top three words are: ")
counter = 0
while counter < 3:
    for word in sorted_dict:
        print(f"{word}: {sorted_dict[word]}")
        counter += 1
        





    

