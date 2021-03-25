import pandas as pd
import glob

merged_history = pd.concat([pd.read_csv(file, parse_dates=True, index_col='UTC time') for file in glob.glob('data/raw_sensor_data/*.csv')])
history = merged_history.sort_index()

history.to_csv("data/full_sensor_data.csv")
