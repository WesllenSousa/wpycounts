
import matplotlib.pyplot as plt

from wpycounts.wpycounts import count_words
from wpycounts.plotting import plot_words

# Inline documentation
# help(plot_words)

counts = count_words("zen.txt")
print(counts)

fig = plot_words(counts, 10)
plt.show()
