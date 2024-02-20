# read version from installed package
from importlib.metadata import version
__version__ = version("wpycounts")

# populate package namespace
from wpycounts.wpycounts import count_words
from wpycounts.plotting import plot_words