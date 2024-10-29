import os
import shutil

from icrawler.builtin import GoogleImageCrawler


def dl_img(keyword:str , name_dir:str, num:int)->None:
    """получает на вход ключевое слово , название файла,куда должны быть скачаны картинки, и количество картинок,
     проверяет наличие файла, загружает картинки с интернета"""
    if os.path.exists(name_dir):
        shutil.rmtree(name_dir)
        os.mkdir(name_dir)
    else:
        os.mkdir(name_dir)

    google_crawler = GoogleImageCrawler(storage={'root_dir': name_dir})
    google_crawler.crawl(keyword=keyword, max_num=num)
