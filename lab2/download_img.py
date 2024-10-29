import os
import shutil

from icrawler.builtin import GoogleImageCrawler


def dl_img(keyword:str , name_dir:str, num:int)->None:
    """
    Function downloads images
    :param keyword: what kind of images are needed to download
    :param name_dir: dir to save images
    :param num: count of images
    :return: None
    """
    if os.path.exists(name_dir):
        shutil.rmtree(name_dir)
        os.mkdir(name_dir)
    else:
        os.mkdir(name_dir)

    google_crawler = GoogleImageCrawler(storage={'root_dir': name_dir})
    google_crawler.crawl(keyword=keyword, max_num=num)
