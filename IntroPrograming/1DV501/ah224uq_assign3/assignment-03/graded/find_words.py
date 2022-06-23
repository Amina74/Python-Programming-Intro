def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().split('\n')
    return lines

def get_words(row):
    words = []
    for word in row.split():
        if word[-1].isalpha() == False:
            word = word[:-1]
        words.append(word.lower())
    return words

def save_words(file_path, words):
    with open(file_path, "w") as file:
        for word in words:
            file.write(word + "\n")

# Read text files
path =  "assignment-03/graded/eng_news_100K-sentences.txt"
rows = read_file(path)
print(f"\nRead {len(rows)} lines from file {path}")

# Collect words
words = []
for row in rows:
    w = get_words(row)  # Returns a list of words
    words += w

# Save words in file
outpath =  f"output_{len(words)}_words.txt"
save_words(outpath,words)
print(f"Saved {len(words)} words in file {outpath}") 