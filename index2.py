import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
range = jumlah_kucing.max() - jumlah_kucing.min()
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
jumlah_kucing_series = pd.Series(jumlah_kucing)
plt.hist(jumlah_kucing, bins=4)

# rata-rata
print(jumlah_kucing.mean())
# median
print(np.median(jumlah_kucing))
# mode atau modus
print(stats.mode(jumlah_kucing)[0])
# range
print(range)
# interquartile range
print(iqr)
# varians
print(jumlah_kucing_series.var().round(2))
# standar deviasi
print(jumlah_kucing_series.std().round(2))
#distribusi normal
plt.show()
# skewness
print(jumlah_kucing_series.skew().round(2))