

left_join_copy = left_join_dailyAct_sleepDate_df.copy()
left_join_copy1 = left_join_copy.copy()
# recommended fix-prob still wrong.
each_ActivityLevel_descrip_forEach_Person = unique_values = left_join_copy1.groupby('Id')['MonthlyActivityLevel'].unique()


# Realization: the current insights im graphing are simple-they only use daily Activity data-
# so no nulls will be present because I left-joined to sleep data. The left table was daily Activity.
# So no need to worry about dropna for this metric. Atleast I hope so, if my reasoning is correct.
id_series = left_join_copy1.index.get_level_values('Id')
#print(id_series.unique())
#print(id_series.name)
#print(type(id_series.name))
almost_visualization_df = left_join_copy1[['MonthlyActivityLevel','AvgMonthlySteps']]
visualization_df = almost_visualization_df.groupby('Id').agg({'MonthlyActivityLevel':'first','AvgMonthlySteps':'mean'})

print(visualization_df.head())
# create list of unique classification values
unique_classifications = visualization_df['MonthlyActivityLevel'].unique()
print(unique_classifications)

#Create a bar plot using Seaborn
sns.barplot(x='Id', y='MonthlyActivityLevel',data=visualization_df,hue='MonthlyActivityLevel')

#Customize the plot
plt.title('Activity Level Classification by Individual')
plt.xlabel('Individual ID')
plt.ylabel('Monthly Activity Level Classification')
plt.xticks(rotation=45)
plt.legend(title='Activity Level')
plt.show()

conditions = [(df_dailyActivity_copy2['TotalSteps'] < 4000), (properlyGrouped_df_copy['TotalSteps'] >= 4000) & (properlyGrouped_df_copy['TotalSteps'] < 8000), (properlyGrouped_df_copy['TotalSteps'] >= 8000) & (properlyGrouped_df_copy['TotalSteps'] < 12000), (properlyGrouped_df_copy['TotalSteps'] >= 12000)]
# make classifications
values = ['Sedentary', 'Lightly', 'Fairly', 'Very']
# generate new col in dataframe
df_dailyActivity_copy2['ActivityLevel'] = np.select(conditions, values)

left_join_dailyAct_sleepDate_df1 = pd.merge(df_dailyActivity_copy2, df_sleepDay_copy, on=['Id','Date'], how='left')


# Distribution of ActivityLevel classifications vs. users
activity_distribution = left_join_dailyAct_sleepDate_df1.groupby('ActivityLevel')['Id'].nunique()

# Plotting the distribution of ActivityLevel vs Users
plt.figure(figsize=(10,6))
activity_distribution.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Distribution of Users by Activity Level')
plt.ylabel('Number of Unique Users')
plt.xlabel('Activity Level')
plt.xticks(rotation=0)
plt.show()

#Average Daily Steps for Each Weekday per User

left_join_dailyAct_sleepDate_df1['ActivityDate'] = pd.to_datetime(left_join_dailyAct_sleepDate_df1['Date'])
left_join_dailyAct_sleepDate_df1['Weekday'] = left_join_dailyAct_sleepDate_df1['Date'].dt.day_name()

# Group by UserId and Weekday to find average daily steps per user for each weekday
avg_steps_per_weekday = left_join_dailyAct_sleepDate_df1.groupby(['Id', 'Weekday'])['TotalSteps'].mean().unstack()

# Plotting average daily steps across weekdays
plt.figure(figsize=(12,6))
sns.heatmap(avg_steps_per_weekday, cmap='Blues', linewidths=0.5)
plt.title('Average Daily Steps for Each Weekday per User')
plt.ylabel('User')
plt.xlabel('Weekday')
plt.xticks(rotation=45)
plt.show()


# User vs. AvgCaloriesBurned (Correlation between ActivityLevel and Calories Burned)

avg_calories_activity = left_join_dailyAct_sleepDate_df1.groupby(['Id', 'ActivityLevel'])['Calories'].mean().unstack()

# Plotting correlation between ActivityLevel and AvgCaloriesBurned for each user
plt.figure(figsize=(10,6))
avg_calories_activity.plot(kind='bar', stacked=True)
plt.title('Correlation between Activity Level and Avg Calories Burned')
plt.ylabel('Avg Calories Burned')
plt.xlabel('UserId')
plt.xticks(rotation=50)
plt.show()

# Alternatively, to check for correlation:
activity_calorie_correlation = left_join_dailyAct_sleepDate_df1.groupby('ActivityLevel')['Calories'].mean()

plt.figure(figsize=(10,6))
activity_calorie_correlation.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Avg Calories Burned per Activity Level')
plt.ylabel('Avg Calories Burned')
plt.xlabel('Activity Level')
plt.xticks(rotation=0)
plt.show()


# Count of Users per Activity Classification vs. Activity Level


# Count the number of users in each classification
activity_classification = left_join_dailyAct_sleepDate_df1.groupby('Id')['ActivityLevel'].value_counts().unstack()

# Plotting the count of users per activity classification
plt.figure(figsize=(10,6))
activity_classification.sum().plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Count of Users per Activity Classification')
plt.ylabel(# Proportion of Daily Step Count to Monthly Total Steps

# Convert 'ActivityDate' to datetime and extract month

left_join_dailyAct_sleepDate_df1['Month'] = left_join_dailyAct_sleepDate_df1['ActivityDate'].dt.month

# Calculate total monthly steps for each user
monthly_steps = left_join_dailyAct_sleepDate_df1.groupby(['Id', 'Month'])['TotalSteps'].sum().reset_index(name='MonthlyTotalSteps')

# Merge with original dataframe to get proportion of daily steps
df = left_join_dailyAct_sleepDate_df1.merge(monthly_steps, on=['Id', 'Month'])

# Calculate proportion of daily steps
df['StepProportion'] = df['TotalSteps'] / df['MonthlyTotalSteps']

# Visualize the change in step proportion over time
plt.figure(figsize=(15,10))
sns.lineplot(x='ActivityDate', y='StepProportion', hue='Id', data=df)
plt.title('Daily Step Proportion to Monthly Total Steps Over Time')
plt.xticks(rotation=45)
plt.show()'Number of Users')
plt.xlabel('Activity Level')
plt.show()


# total steps vs average sleep hours scatter plot

steps_sleep_df = left_join_dailyAct_sleepDate_df1.groupby(['Id','ActivityLevel']).agg({
    'TotalSteps': 'sum',
    'TotalSleepRecords': 'mean'
}).reset_index()

# Plotting Total Steps vs Average Sleep Hours
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TotalSteps', y='TotalSleepRecords', data=steps_sleep_df,hue='ActivityLevel')

# Add title and labels
plt.title('Total Steps vs. Average Sleep Hours per Employee')
plt.xlabel('Total Steps')
plt.ylabel('Average Sleep Hours')
plt.grid(True)

# Show the plot
plt.show()


