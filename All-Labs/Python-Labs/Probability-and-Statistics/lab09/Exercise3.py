import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

"""    
In the serene embrace of the early morning, a world wrapped in the soft hues of dawn unfolds with the delicate beauty of nature awakening—sunlight piercing the darkness, birds orchestrating a harmonious symphony, dew-kissed grass shimmering like diamonds—a tranquil interlude that invites introspection and reflection on the profound magic woven into the fabric of each passing moment, urging us to embrace the present and find solace in the simplicity of existence.
"""

# enter a text from user
text = str(input("Enter a text: "))

# spilt text with ""
splited_text = text.split(" ")
key_list = Counter(splited_text)

for key in splited_text:
    key_list[key] = splited_text.count(key)

most_appearance_word = key_list.most_common(30)

x = [word[0] for word in most_appearance_word]
y = [word[1] for word in most_appearance_word]

fig, ax = plt.subplots(1, 1)
plt.plot(x, y)
plt.xlabel("Words")
plt.ylabel("Appearance")
plt.show()
