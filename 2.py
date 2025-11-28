import pandas as pd
import matplotlib.pyplot as plt

data = [['letadlo', 57, 'dolet'],
['auto', 23, 'spotřeba'],
['loď', 91, 'náklad'],
['most', 12, 'nosnost'],
['počítač', 84, 'paměť'],
['dům', 47, 'plocha'],
['strom', 68, 'stáří'],
['kolo', 35, 'průměr'],
['raketa', 99, 'palivo'],
['vlk', 41, 'teritorium'],
['mobil', 76, 'výdrž'],
['město', 63, 'rozloha'],
['robot', 54, 'moduly'],
['vlak', 17, 'rychlost'],
['kamera', 88, 'snímač'],
['řeka', 25, 'průtok'],
['planeta', 49, 'obvod'],
['motor', 32, 'výkon'],
['kniha', 70, 'počet stran'],
['pes', 11, 'věk']]

df = pd.DataFrame(data, columns=['objekt', 'hodnota', 'vlastnost'])
print(df.head())
df_filtered = df[df['hodnota'] > 50]
print(df_filtered)
df_sorted_asc = df.sort_values(by='hodnota')
print(df_sorted_asc)

stats = df['hodnota'].describe()
print(stats)

# Jednotlivé statistiky
print("Průměr:", df['hodnota'].mean())
print("Minimum:", df['hodnota'].min())
print("Maximum:", df['hodnota'].max())
print("Medián:", df['hodnota'].median())


plt.hist(df['hodnota'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram hodnot druhého sloupce')
plt.xlabel('Hodnota')
plt.ylabel('Počet objektů')
plt.show()