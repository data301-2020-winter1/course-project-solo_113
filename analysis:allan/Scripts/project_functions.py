import pandas as pd
import numpy as np


def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
         pd.read_csv('fatal-police-shootings-data.csv')
           .drop(['latitude', 'longitude', 'is_geocoding_exact', 'manner_of_death', 'flee'], axis=1)
           .rename(columns={'race': 'ethnicity'})
          
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
        .assign(armed= lambda x: np.where(x['armed']=='unarmed', False, True))
        .assign(threat_level= lambda x: np.where(x['threat_level']=='attack', True, None))
        .assign(Armed_Attack= lambda x: np.where(x['armed']== x['threat_level'], True, False))
        .reset_index(drop=True)
    )
      

    # Make sure to return the latest dataframe

    return df2 
