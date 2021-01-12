import requests
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer


def data_collector(url, filename):
    data = requests.get(url)

    with open(filename, 'w') as f:
        f.write(data.text)


def int_to_dt(dates):
    plt_dates = dates.copy()
    plt_dates = plt_dates.reshape(-1)
    plt_dates = plt_dates.astype(np.int)

    plt_dates = pd.to_datetime(plt_dates.astype(str)).values

    return plt_dates


def build_feature_matrix(filename):

    # The dates have to first be imported as strings so the apostrophes and hyphens can be stripped before they can be converted into integers.
    dates = np.genfromtxt(filename, delimiter=',', usecols=3, skip_header=1, dtype=str, missing_values='')
    dates = np.char.strip(dates, '"')
    dates = np.char.replace(dates, '-', '')
    dates = dates.astype(np.int)
    dates = dates[:, np.newaxis]

    data = np.genfromtxt(filename, delimiter=',', usecols = (6, 8, 9, 10), skip_header=1, dtype=str,)
    data = np.char.strip(data, '"')
    data = np.where(data=='', np.nan, data)
    data = data.astype(float)

    lines = int(data.size / 4)
    data.reshape([lines, 4])

    # All missing data is replaced with the mean for its column. The sklearn models do not accept nan values.
    imp = SimpleImputer(strategy='mean')
    data = imp.fit_transform(data)

    x = np.hstack([dates.copy(), data.copy()])

    return x


def build_target_array(filename):
    y = np.genfromtxt(filename, delimiter=',', usecols=7, skip_header=1, dtype=str)
    y = np.char.strip(y, '"')
    y = np.where(y=='', np.nan, y)
    y = y.astype(float)

    y = y[:, np.newaxis]
    
    # All missing data is replaced with the mean for its column. The sklearn models do not accept nan values.
    imp = SimpleImputer(strategy='mean')
    y = imp.fit_transform(y)

    return y