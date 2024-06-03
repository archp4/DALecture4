import pandas as pd


def replace_missing_value_with_mean(dataframe, label, column):
    # dataframe[column] = dataframe[column].groupby(label).transfrom(lambda x: x.fillna(x.mean()))
    dataframe[column] = dataframe[column].fillna(dataframe[column].groupby(label)[column].transfrom('mean'))
    return dataframe
