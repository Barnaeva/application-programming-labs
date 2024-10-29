import csv
import os

def mk_annotation(name_dir:str, name_file:str)->None:
    """создает файл аннотации перед этим проверяет существует ли такой"""
    data = []
    for name in os.listdir(name_dir):
        abs_path=os.path.abspath(name)
        rel=os.path.join(name_dir,name)
        data.append([abs_path,rel])

    if os.path.exists(name_file):
        os.remove(name_file)

    with open(name_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
