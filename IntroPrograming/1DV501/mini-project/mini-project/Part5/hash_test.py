'''

This file contains the tests and graphs for the hash set

'''
import HashSet as hset
import time
from matplotlib import pyplot as plt

# Open the file and read all the contents, store them in a list
file = open('eng_news_100K-sentences.txt', encoding="UTF-8")
words = []
while len(words) <= 1000:
    line = file.readline()

    line = line.strip().split()
    for word in line:

        if word not in words:
            words.append(word)

file.close()

# create lists of labels of various sample sizes
sizes_1000_words = []
for i in range(1, 1001):
    sizes_1000_words.append(i)

sizes_50_words = sizes_1000_words[0:50]
sizes_100_words = sizes_1000_words[0:100]
sizes_500_words = sizes_1000_words[0:500]
sizes_1000_words = sizes_1000_words[0:1000]

# create lists of the time taken by various sample sizes
times_50_words = []
times_100_words = []
times_500_words = []
times_1000_words = []
max_bucket_sizes = []
count = 0

# initialize the hashset
map = hset.HashSet()
map.init()

# for each word in the list of words, add it to the
# hash map and measure the time taken. Add the values to
# their respective lists
start_time = time.time()

for word in words:
    map.add(word)
    end_time = time.time()
    count += 1
    if count <= 50:
        times_50_words.append(round(end_time-start_time, 3))

    if count <= 100:
        times_100_words.append(round(end_time-start_time, 3))
    if count <= 500:
        times_500_words.append(round(end_time-start_time, 3))
    if count <= 1000:
        times_1000_words.append(round(end_time-start_time, 3))
        max_bucket_sizes.append(map.max_bucket_size())


# plot the graphs
plt.plot(sizes_50_words, times_50_words)
plt.title("scaling of time with number of inputs (50) inputs")
plt.ylabel('time(s)')
plt.xlabel('number of inputs')
plt.show()

plt.plot(sizes_100_words, times_100_words)
plt.title("scaling of time with number of inputs (100) inputs")
plt.ylabel('time(s)')
plt.xlabel('number of inputs')
plt.show()

plt.plot(sizes_500_words, times_500_words)
plt.title("scaling of time with number of inputs (500) inputs")
plt.ylabel('time(s)')
plt.xlabel('number of inputs')
plt.show()

plt.plot(sizes_1000_words, times_1000_words)
plt.title("scaling of time with number of inputs (1000) inputs")
plt.ylabel('time(s)')
plt.xlabel('number of inputs')
plt.show()


plt.plot(sizes_1000_words, max_bucket_sizes)
plt.title("scaling of bucket size with number of inputs (1000) inputs")
plt.ylabel('max bucket size')
plt.xlabel('number of inputs')
plt.show()
