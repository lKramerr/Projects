import random

list_word1 = ["R", "E", "S", "T", "A", "U", "R", "A", "N", "T"]
list_word2 = ["I", "N", "D", "E", "P", "E", "N", "D", "E", "N", "C", "E"]
list_word3 = ["A", "U", "X", "I", "L", "I", "A", "R", "I", "E", "S"]

list_words = [list_word1, list_word2, list_word3]
list_word_fill = []

int_word = random.choice(list_words)

for n in int_word:
    list_word_fill.append("_")

