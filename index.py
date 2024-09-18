import pandas as pd
from scipy import stats

jumlah_kucing = pd.Series([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

mode_jumlah_kucing = stats.mode(jumlah_kucing)

print("Mean:", jumlah_kucing.mean())  # Mean
print("Median:", jumlah_kucing.median())  # Median
print("Mode:", mode_jumlah_kucing.mode)  # Mode
print("Mode Count:", mode_jumlah_kucing.count)  # Mode Count

