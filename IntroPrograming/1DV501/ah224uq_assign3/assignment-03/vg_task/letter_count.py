import math


def count(lst):
    total = len(lst)
    letter = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
              'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for sentence in lst:
        for word in sentence:
            char = word.lower()
            if len(char) == 1:
                if 97 <= ord(char) <= 122:
                    if char in letter:
                        num = letter[char] + 1
                        letter[char] = num
                    else:
                        letter[char] = 1

    print("Total number of letters: ", total)
    return letter


def make_histogram(letter):
    max_value = max(letter, key=lambda x: letter[x])
    max_value = letter[max_value]
    scale = 10 / max_value

    print("\nHistogram (where each star represents ", math.floor(max_value / 10), " occurrences)")

    for key, value in letter.items():

        print(key, end=" | ")
        upper_limit = math.floor(scale * value)
        for i in range(0, upper_limit):
            print("*", end="")
        print("")

    print("")


def read_file(location):
    print("Reading text from file: ", location)
    lst = []
    with open(location, 'r') as file:
        for line in file:
            row = line.strip()
            lst.append(row)

    letter = count(lst)
    print(letter)
    make_histogram(letter)


read_file("assignment-03/graded/holy_grail.txt")
read_file("assignment-03/graded/eng_news_100K-sentences.txt")
