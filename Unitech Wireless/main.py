import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('422k-Unitech_Wireless.csv', on_bad_lines='warn', names=['col1', 'col2', ..., 'col10'])

print(df)

profile = ProfileReport(df)
profile.to_file(output_file="unitech.html")