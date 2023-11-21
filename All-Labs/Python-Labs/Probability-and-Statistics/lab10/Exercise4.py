import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# get the text from user
text = input("Input a text: ")

# split text from " "
spilted_text = text.split(" ")
key_list = Counter(spilted_text)

# count all the word in from the input text
for key in key_list:
    key_list[key] = spilted_text.count(key)

# get the first 30 common words
most_appearance_word = key_list.most_common(30)

x = [word[0] for word in most_appearance_word]

# plot the most appearance word follow the histogram
fig, ax = plt.subplots(1, 1)

ax.hist(x, bins=[0, 30, 60, 90])
ax.set_title("Histogram of most appearance word")
ax.set_xticks([0, 30, 60, 90])
ax.set_xlabel("words")
ax.set_ylabel("no. of word")
plt.show()
