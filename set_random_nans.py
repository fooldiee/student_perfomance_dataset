from numpy.random import rand
import pandas as pd
import numpy as np


def set_random_nans(df):
    p = 0.005
    mask = np.random.choice([True, False], size=df.shape, p=[p, 1 - p])
    new_df = df.mask(mask)
    return new_df