import pandas as pd

df = pd.read_csv("spotify_history.csv")
#print(df.head())
#df.info()
#print(df.describe())
#print(df.columns)


#print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

#Checking for missing values
print(df.isnull().sum())


# Find rows where either 'reason_start' or 'reason_end' is missing
#missing_either = df[df['reason_start'].isnull() | df['reason_end'].isnull()]
#print(missing_either)

# Save to CSV
#missing_either.to_csv("missing_reasonnns.csv", index=True)



#Since the Values are categorical, i'll use unknown instead of just deleting the rows
df['reason_start'] = df['reason_start'].fillna("unknown")
df['reason_end'] = df['reason_end'].fillna("unknown")


df.to_csv("MisssingValuesHandled.csv", index=False)
