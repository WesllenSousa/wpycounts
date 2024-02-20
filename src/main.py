
import matplotlib.pyplot as plt

#import wpycounts
#counts = wpycounts.count_words("zen.txt")
#print(counts)

from wpycounts.wpycounts import count_words
from wpycounts.plotting import plot_words
from wpycounts.datasets import get_flatland

# Inline documentation
# help(plot_words)

flatland = get_flatland()
counts = count_words(flatland)
print(counts)

fig = plot_words(counts, 10)
# plt.show()