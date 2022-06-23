import os

# opening text files, reading the text and converting the text into list
# data of first file
dataA = open("mini-project/Part1/eng_news_100K-sentences.txt", encoding="utf8").read().split()
# data of second file
dataB = open("mini-project/Part1/holy_grail.txt", encoding="utf8").read().split()

# 1. finding the total unique words using list.

# listA is used to save unique words
uniq = []
# iterate the data of first file
for word in dataA:
    # if the word is not in unique words list then add it to it.
    if word not in uniq:
        uniq.append(word)

# iterate the data of second file
for word in dataB:
    # if the word is not in unique words list then add it to it.
    if word not in uniq:
        uniq.append(word)

# printing the unique words
print("the total unique words are: ", len(uniq))

#  generate top 10 most frequent words
# joining both files data
data = dataA + dataB
# setting frequency to zero
frequency = [0] * len(uniq)
s = list(uniq)

# iterating whole data
for w in data:
    # counting frequency
    frequency[s.index(w)] = frequency[s.index(w)] + 1

# printing the top 10 words
print("the top 10 most frequent words are given blow")
i = 10
while i:
    # get index of max frequent number
    maxindex = frequency.index(max(frequency))
    # if the length is greater than 4
    if len(s[maxindex]) > 4:
        # print the string
        print(s[maxindex], max(frequency))
        i = i - 1
    # pop the values form index
    s.pop(maxindex)
    frequency.pop(maxindex)