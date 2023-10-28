import pandas as pd

def read_file(file_path, delimiter=','):
    """
    Read a CSV file and return its content as a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.
        delimiter (str): The delimiter used in the CSV file (default is ',' for comma-separated).

    Returns:
        pandas.DataFrame: A Pandas DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_dataframe_to_csv(dataframe, file_path, index=False):
    """
    Write a Pandas DataFrame to a CSV file.

    Args:
        dataframe (pandas.DataFrame): The DataFrame to be written to a CSV file.
        file_path (str): Path to the output CSV file.
        index (bool): Whether to write the DataFrame index (default is False).
    """
    try:
        dataframe.to_csv(file_path, index=index)
        print(f"DataFrame written to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

