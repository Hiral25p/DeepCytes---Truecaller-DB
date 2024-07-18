import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv('9M-Aircel.csv')
print(df)

profile=ProfileReport(df)
profile.to_file(output_file="telenor.html")
