import argparse

from annotation import mk_annotation
from download_img import dl_img
from iterator import MyIterator


def pars() -> tuple[str, int, str, str]:
    """парсер запрашиваеет с терминала название картинок, папки,  файла аннотации и количество картинок """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help='name img pls')
    parser.add_argument('-nm', '--num', type=int, help='the num img pls')
    parser.add_argument('-nd','--name_dir', type=str, help='name dir pls')
    parser.add_argument('-nf','--name_file', type=str, help='name img pls')

    args = parser.parse_args()

    return args.keyword, args.num, args.name_dir, args.name_file


def main():
    keyword, num, name_dir, name_file = pars()
    try:
        dl_img(keyword,name_dir,num)
        mk_annotation(name_dir,name_file)
        my_iter=MyIterator(name_dir)
        for img in my_iter:
            print(img)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__=="__main__":
    main()

