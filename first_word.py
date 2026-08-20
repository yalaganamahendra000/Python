sentence = input("Enter your sentence: ")

sentence = sentence.lower()
words = sentence.split()

n = words[0]

for i in range(1, len(words)):
    if words[i] < n:
        n = words[i]

print(n)