'''
This file contains the tests and graphs for the binary search tree

'''

from BstMap import bst
import time
from matplotlib import pyplot as plt

# Open the file and read all the contents, store them in a list
file = open('eng_news_100K-sentences.txt', encoding="UTF-8")
lines = []
for i in range(20000):
    line = file.readline()
    lines.append(line.strip().split("\t", 1))
file.close()

# create a list of 20000 sample labels
sizes = []
for i in range(1, 21):
    sizes.append(i*1000)


times = []
max_depths = []
count = 0
map = bst.BstMap()

# for each key, value pair in the list of lines, add it to the
# binary search tree and measure the time taken. Add the values to
# the list of times taken at intervals of 1000 samples
start_time = time.time()
for line in lines:
    map.put(line[0], line[1])
    count += 1
    if count % 1000 == 0:
        max_depths.append(map.max_depth())
        end_time = time.time()
        times.append(round(end_time-start_time, 3))


# plot the charts
plt.plot(sizes, times)
plt.title("scaling of time with number of inputs")
plt.ylabel('time(s)')
plt.xlabel('number of inputs')
plt.show()

plt.plot(sizes, max_depths)
plt.title("scaling of max tree depth with number of inputs")
plt.ylabel('max tree depth')
plt.xlabel('number of inputs')
plt.show()
