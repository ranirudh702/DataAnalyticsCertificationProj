
#Start of cleaning activities
#-----------------------------------------------------------------------

#Start Cleaning for df_dailyActivity_copy

# check the data for repeats and nulls
# Before changing names of columns and dtypes of columns, do important checks for nulls or repeated values. Find out why if they exist.
print(df_dailyActivity_copy.isna().sum())
print(df_dailyActivity_copy.duplicated().sum())
# Confirmed that there are no nulls or repeated values for dailyActivity df.

# Now standardizing column name and dtypes for the column that signifies date.
df_dailyActivity_copy.rename(columns={'ActivityDate':'Date'}, inplace=True)
df_dailyActivity_copy['Date'] = pd.to_datetime(df_dailyActivity_copy['Date'], format='%m/%d/%Y')
print("Num unique Ids in dailyActivity dataset: ",df_dailyActivity_copy['Id'].nunique())
df_dailyActivity_copy['Id'] = df_dailyActivity_copy['Id'].astype(str) # don't want weird behaviors when grouping df, which could happen if it is a int type.
print(df_dailyActivity_copy.info())

# spot-check if it seems good.
df_dailyActivity_copy.head()

# num unique people measured for in dailyActivity
#I added the print function around it. Originally was in it's own code cell in Colab
print(df_dailyActivity_copy['Id'].nunique())

# Make a new column in the dataframe thats a copy of dailyActivity that mentions what day of week each day of month is.
df_dailyActivity_copy['DayOfWeek'] = df_dailyActivity_copy.Date.dt.day_name()
# check to make sure the days of the week in the newly created column are strings.
print(type(df_dailyActivity_copy['DayOfWeek'][1])) # good

# Note: The maximally independent column of data in the dailyActivity_copy dataframe is the date col, since we are measuring over a month time period for each person.
# Want to group by person(Id) AND date. Reason for this: Each person used in the study has data measured over same month (each day of the measured month has data for that person), so I want to structure df w/samee paradigm.
groupby_person_date_combo = df_dailyActivity_copy.groupby(['Id','Date'])

# create copy of df_dailyActivity_copy because you are going to add to new cols to it and merge with another df in future for ur analysis
df_dailyActivity_copy2 = df_dailyActivity_copy.copy()
print(groupby_person_date_combo.head())
# I thought grouping by Id and Date would group it in such a way that each Id would have all the
# days for that person. In other words, I thought the repeated vals for Id would go away. It seems not

# I guess I need to aggregate each data column after the Id & Date columns so that the dataframe
# is grouped in the way I visualized.


# Cleaning SleepData
#-------------------------------------------------------------------------------
df_sleepDay_copy.head()
df_sleepDay_copy1 = df_sleepDay_copy.copy()

# Now check for nulls and repeats. If present, find out which ones, where, and why
#print(df_sleepDay_copy.isna().sum())
#print(df_sleepDay_copy.duplicated().sum()) # there are 3 duplicates.
duplicate_rows = df_sleepDay_copy[df_sleepDay_copy.duplicated()]
#print("Duplicate Rows:")
#print(duplicate_rows)
#print(df_sleepDay_copy.head())
# So I've isolated the duplicate rows and I know which index/where/which ones they are.
# Will now take a novel approach, and not try to manually scrub the repeats from sleepDay df like I did in last attempt. Instead leverage groupby
# for unique values/groupings and choose proper fields to group by so that newly grouped df is guaranteed to not have repeats.


# first clean sleepDay column by changing dtype from object to datetime, change name to Date, and model date w/same format as dailyActivity df.
df_sleepDay_copy.rename(columns={'SleepDay':'Date'}, inplace=True)
#create function to extract date portion from date and discard time portion and turn back into datetime.
def extract_date_portion(date_string):
  #split string and return only first part
  return pd.to_datetime(date_string.split()[0], format='%m/%d/%Y')
df_sleepDay_copy['Date'] = df_sleepDay_copy['Date'].apply(extract_date_portion)
df_sleepDay_copy['Id'] = df_sleepDay_copy['Id'].astype(str)
# Add dayofweek column to sleepDay. Will prob be useful for metrics/vizes that compare user sleep on certain days of week and make user-level marketing recs.
df_sleepDay_copy['DayOfWeek'] = df_sleepDay_copy.Date.dt.day_name()
# Now check that col dtypes and names are good.
print(df_sleepDay_copy.info()) # good. Now do novel approach and create unique grouped df
print(df_sleepDay_copy.head())

# Now create unique grouped df.
sleepDay_Id_Date_grouping = df_sleepDay_copy.groupby(['Id','Date'])
properlyGroupedSleepDay_df = sleepDay_Id_Date_grouping.agg({'TotalSleepRecords':'mean','TotalMinutesAsleep':'mean','TotalTimeInBed':'mean','DayOfWeek':'first'})
# Convert 'Date' index to datetime
properlyGroupedSleepDay_df.index = properlyGroupedSleepDay_df.index.set_levels(pd.to_datetime(properlyGroupedSleepDay_df.index.levels[1]), level=1)
print(properlyGroupedSleepDay_df.head())
properlyGroupedSleepDay_df2 = properlyGroupedSleepDay_df.copy()