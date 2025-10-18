import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("MisssingValuesHandled.csv")

df['ts'] = pd.to_datetime(df['ts'])

df['hour'] = df['ts'].dt.hour

df['day'] = df['ts'].dt.day_name()
df['month'] = df['ts'].dt.month_name()
df['year'] = df['ts'].dt.year

print(df['year'].value_counts().sort_index())


print(df.dtypes)
print(df.columns)
df.head()
df.info()

#Timestamp
#from datetime import datetime
#timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#filename = f"time_analysis_{timestamp}.csv"
#df.to_csv(filename, index=False)


import seaborn as sns
import matplotlib.pyplot as plt

#total dataset
hourly = df['hour'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly.index, y=hourly.values, marker='o')
plt.title("Listening Pattern by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Plays")
plt.grid(True)
plt.show()

#Average time per day
# First, extract the date (not time) from the timestamp
df['date'] = df['ts'].dt.date

# Now group by date and hour
hourly_daily = df.groupby(['date', 'hour']).size().reset_index(name='play_count')

# Then calculate average number of plays for each hour across all days
average_hourly = hourly_daily.groupby('hour')['play_count'].mean()

# Plot
import matplotlib.pyplot as plt

average_hourly.plot(kind='line', marker='o', figsize=(10, 5))
plt.title("Average Plays by Hour Per Day")
plt.xlabel("Hour of Day")
plt.ylabel("Average Number of Plays")
plt.grid(True)
plt.show()


#Monthly trend
df['month'] = pd.Categorical(df['month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True)

monthly = df['month'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.barplot(x=monthly.index, y=monthly.values)
plt.title("Listening Trend by Month")
plt.xlabel("Month")
plt.ylabel("Number of Plays")
plt.xticks(rotation=45)
plt.show()

#monthly values with labels
import matplotlib.pyplot as plt

# Get value counts sorted by month name
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

month_counts = df['month'].value_counts().reindex(month_order)

# Plot
ax = month_counts.plot(kind='bar', figsize=(14, 6))
plt.title("Listening Trend by Month")
plt.xlabel("Month")
plt.ylabel("Number of Plays")
plt.xticks(rotation=45)

# Add value labels
for i, value in enumerate(month_counts):
    ax.text(i, value + 300, str(value), ha='center', fontsize=9)

plt.tight_layout()
plt.show()


####

import pandas as pd
import matplotlib.pyplot as plt

# Ensure timestamp is in datetime format
df['ts'] = pd.to_datetime(df['ts'])

# Extract month name and year
df['month'] = df['ts'].dt.month_name()
df['year'] = df['ts'].dt.year

# To maintain calendar order
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Group by year and month
monthly_trend = df.groupby(['year', 'month']).size().unstack(fill_value=0)
monthly_trend = monthly_trend[month_order]  # reorder months

# Plot stacked bar chart
ax = monthly_trend.T.plot(
    kind='bar',
    stacked=True,
    figsize=(14, 8),
    colormap='tab20c'
)

# Add labels on top of each stacked segment
#for bars in ax.containers:
 #   ax.bar_label(bars, label_type='center', fontsize=8, color='white')

# Add title and labels
plt.title("Monthly Listening Trend by Year")
plt.xlabel("Month")
plt.ylabel("Number of Plays")
plt.xticks(rotation=45)
plt.legend(title="Year", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()


#top artists over 5 months

# Top 5 artists overall
top5_artists = df['artist_name'].value_counts().head(5).index

# Group plays by month and artist
artist_monthly = df[df['artist_name'].isin(top5_artists)].groupby(
    [df['ts'].dt.month_name(), 'artist_name']
).size().unstack(fill_value=0)

# Reorder months
artist_monthly = artist_monthly.reindex(month_order)


#yearly trend
yearly = df['year'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
sns.barplot(x=yearly.index, y=yearly.values)
plt.title("Listening Trend by Year")
plt.xlabel("Year")
plt.ylabel("Number of Plays")
plt.show()

