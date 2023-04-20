from collections import defaultdict

document = "the quick brown fox jumps over the lazy dog"

word_count = defaultdict(int)
for word in document.split():
    word_count[word] += 1

print(word_count)
