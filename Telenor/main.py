import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv('404k-Telenor.csv')
print(df)

profile=ProfileReport(df)
profile.to_file(output_file="telenor.html")