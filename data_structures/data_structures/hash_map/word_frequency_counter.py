# ---------------------------------------------------------
# Program: Word Frequency Counter
# Description:
# This program counts the frequency of each word in a sentence.
# ---------------------------------------------------------

sentence = "python is powerful and python is easy and python is popular"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:")
for word, count in word_count.items():
    print(word, ":", count)
