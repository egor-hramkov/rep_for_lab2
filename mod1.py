import numpy as np

f = open('D://nado/ABBREV.csv', 'r', encoding='utf8')
table = np.genfromtxt(f, delimiter=';', dtype=None, names=True, encoding="utf8")
f.close()

a = np.array(table)

kkal = np.sort(a, axis=-1, kind='quicksort', order=['Energ_Kcal', 'Shrt_Desc'])[::-1]
sugar = np.sort(a, axis=-1, kind='quicksort', order=['Sugar_Tot_g', 'Shrt_Desc'])
protein = np.sort(a, axis=-1, kind='quicksort', order=['Protein_g'])[::-1]
vit_c = np.sort(a, axis=-1, kind='quicksort', order=['Vit_C_mg'])[::-1]

print(kkal[0][1])
print(sugar[0][1])
print(protein[0][1])
print(vit_c[0][1])
