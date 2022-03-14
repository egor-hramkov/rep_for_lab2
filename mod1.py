import re
from operator import itemgetter
import numpy as np

with open('ABBREV.csv', 'r', newline='') as f:
    table = np.genfromtxt(f, delimiter=';', dtype=None, names=True, encoding="utf8")

a = np.array(table)

kkal = np.sort(a, axis=-1, kind='quicksort', order=['Energ_Kcal', 'Shrt_Desc'])[::-1]
sugar = min(table, key=itemgetter(9))[9]
list_sugar = [i for i, j in enumerate(table) if j[9] == sugar]
protein = np.sort(a, axis=-1, kind='quicksort', order=['Protein_g', 'Shrt_Desc'])[::-1]
vit_c = np.sort(a, axis=-1, kind='quicksort', order=['Vit_C_mg'])[::-1]

print(kkal[0][1])
print([sorted([table[i][1] for i in list_sugar], key=lambda x: re.sub('[^A-Za-z]+', '', x))[0]])
print(protein[0][1])
print(vit_c[0][1])
