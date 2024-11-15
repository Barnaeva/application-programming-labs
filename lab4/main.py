import argparse
from DataFrame import make_df, add_shape, static_data, fil_df, new_par, sort_df, plot_area_histogram

def pars() -> (str, int, int):
    parser = argparse.ArgumentParser(description='Process an image with optional rotation.')
    parser.add_argument('name_file', type=str, help='name file with annotation please')
    parser.add_argument('-mw', '--max_width', type=int, help='max width please', default=None)
    parser.add_argument('-mh', '--max_height', type=int, help='max height please', default=None)
    args = parser.parse_args()
    return args.name_file, args.max_width, args.max_height

def main():
    try:
        name_file, max_width, max_height = pars()
        df = make_df(name_file)
        print(f'\nDataFrame\n{df}')

        add_shape(df)
        print(f'\nUpdated DataFrame\n{df}')

        stat = static_data(df)
        print(f'\nStatic data\n{stat}')

        if max_width is not None and max_height is not None:
            filter_df = fil_df(max_width, max_height, df)
            print(f'\nFiltered DataFrame\n{filter_df}')
        else:
            print("Max width and max height is None :(")

        new_par(df)
        print(f'\nUpdated DataFrame with Area\n{df}')

        sorted_df = sort_df(df)
        print(f'\nSorted DataFrame\n{sorted_df}')

        plot_area_histogram(df)

    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()