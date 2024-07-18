import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
import pandas as pd
from ydata_profiling import ProfileReport

file_path = '19M-BSNL_Mobile.csv'

# Specify the data types for specific columns
dtype_spec = {0: 'str', 4: 'str', 8: 'str', 9: 'str'}

# Load the CSV file
df = pd.read_csv(file_path, dtype=dtype_spec, low_memory=False, on_bad_lines='skip')

# Fill missing values with 'missing'
df.fillna(value='missing', inplace=True)

# Ensure no NoneType in categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].astype(str).apply(lambda x: 'missing' if pd.isna(x) or x == 'None' else x)

# Generate the profiling report with minimal configuration
profile = ProfileReport(df, title="Pandas Profiling Report", minimal=True)

# Save the report to an HTML file
profile.to_file("output.html")