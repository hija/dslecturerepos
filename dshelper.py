import pandas as pd
import numpy as np
import random

def load_unpreprocessed_dataset():
    df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')
    
    # let's make it reproducible
    random.seed(42)
    
    # Add some null values...
    # First we set some countries to NULL
    indices_country = random.choices(list(range(len(df))), k = 3)
    # Change the value to nan
    df.loc[indices_country, 'country'] = np.nan
    
    # Set some beer savings to NULL
    indices_beer_servings = random.choices(list(range(len(df))), k = 3)
    df.loc[indices_beer_servings, 'beer_servings'] = np.nan
    
    return df