# WAP to ask for a sentence and count the number of words

sentence = input("Please enter a sentence: ")

words = sentence.split()

count = len(words)

print(words)
print("Number of words is :", count)
