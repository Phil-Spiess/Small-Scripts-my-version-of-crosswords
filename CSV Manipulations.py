##https://www.kaggle.com/datasets/usamabuttar/significant-earthquakes

import pandas as pd

earthquake_df = pd.read_csv('Earthquakes.csv')
print(earthquake_df[(earthquake_df['mag'] == earthquake_df['mag'].max())])