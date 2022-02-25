import numpy as np
import csv
import os
from os.path import getsize, join

def get_files_sizes(dirpath):
    if os.path.exists(dirpath):
        os.chdir(dirpath)
        for root, dirs, files in os.walk('.'):
            for i in files:
                if os.path.isfile(join(dirpath, i)):
                    razmer = "bytes"
                    count_razmer = 0
                    total_size = getsize(join(dirpath, i))
                    while total_size > 1024:
                        total_size /= 1024
                        count_razmer += 1
                    match(count_razmer):
                        case(1):
                            razmer = "KB"
                        case (2):
                            razmer = "MB"
                        case (3):
                            razmer = "GB"
                    print(i, total_size, razmer)
    else:
        print("Данная директория не найдена!")
#get_files_sizes("D://nado")

os.chdir('.')
name = input()
if os.path.exists(name):
    with open(name, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"')
        table = np.genfromtxt(f, delimiter=';', dtype=None, names=True, encoding="utf8")
    a = np.array(table)

    sorts = np.sort(a, axis=-1, kind='quicksort', order=['price'])[::-1]
    print(sorts)

