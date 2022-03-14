import numpy as np
import csv
import os
import json
from datetime import datetime
from os.path import getsize, join

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

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

    sort_price = np.sort(a, axis=-1, kind='quicksort', order=['price'])[::-1]
    sort_data = sorted(a, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y %H:%M'))

    datas = {
        'Поездка': [],
        'Начало поездки': [],
        'Конец поездки': [],
        'Телефон': [],
        'Километраж': [],
        'Цена': []
    }

    print("Сортировка по цене поездки: ", sort_price)
    print("Сортировка по дате поездки: ",sort_data)
    print("Сортировка по критерию: ")
    for i in table:
        if(i[4] > 10):
            print(i)
            datas['Поездка'].append(i[0])
            datas['Начало поездки'].append(i[1])
            datas['Конец поездки'].append(i[2])
            datas['Телефон'].append(i[3])
            datas['Километраж'].append(i[4])
            datas['Цена'].append(i[5])

    with open("data.json", "w") as write_file:
        json.dump(datas, write_file,  cls=NpEncoder, ensure_ascii=False)
        os.replace(write_file, "../")
    #os.remove(name)
else:
    print("Данный файл не найден!")


