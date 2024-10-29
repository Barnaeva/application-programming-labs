import csv
import os

def mk_annotation(name_dir:str, name_file:str)->None:
    """
    Function creates annotation file for images with rel and abs paths
    :param name_dir: dir with images
    :param name_file: name for annotation file
    :return: None
    """
    data = []
    for name in os.listdir(name_dir):
        rel=os.path.join(name_dir,name)
        abs_path=os.path.abspath(rel)
        data.append([abs_path,rel])

    if os.path.exists(name_file):
        os.remove(name_file)

    with open(name_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
