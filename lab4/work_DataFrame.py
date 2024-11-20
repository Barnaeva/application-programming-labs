import cv2
import matplotlib.pyplot as plt
import pandas as pd


def make_df(name_file: str) -> pd.DataFrame:
    """
    Load a CSV file and create a DataFrame

    :param name_file: Path to the CSV file
    :return: DataFrame
    """
    df = pd.read_csv(name_file, header=None)
    df.columns = ['Absolute_Path', 'Relative_Path']
    return df


def add_shape(df: pd.DataFrame) -> None:
    """
    Add columns height, width, depth  to the DataFrame

    :param df: DataFrame with image paths
    :return: None
    """
    for i, path in enumerate(df["Relative Path"]):
        my_img = cv2.imread(path)
        height, width, depth = my_img.shape

        df.at[i, "Height"] = height
        df.at[i, "Width"] = width
        df.at[i, "Depth"] = depth



def static_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return statistics of image dimensions

    :param df: DataFrame
    :return: Statistics
    """
    return df[['Height', 'Width', 'Depth']].describe()


def fil_df(max_width: int, max_height: int, df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter DataFrame by maximum dimensions

    :param max_width: Max width
    :param max_height: Max height
    :param df: DataFrame
    :return: Filtered DataFrame
    """
    return df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]


def new_par(df: pd.DataFrame) -> None:
    """
    Add a column for image area

    :param df: DataFrame
    :return: None
    """
    df["Area"] = df['Height'] * df['Width']


def sort_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort DataFrame by image area

    :param df: DataFrame
    :return: Sorted DataFrame
    """
    return df.sort_values(by='Area')


def plot_area_histogram(df: pd.DataFrame) -> None:
    """
    Creating a histogram in the area column

    :param df: DataFrame
    :return: None
    """
    plt.figure()

    df['Area'].diff().hist()

    plt.title('Histogram of areas')
    plt.xlabel('Area')
    plt.ylabel('Count')

    plt.show()
