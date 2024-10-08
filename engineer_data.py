properlyGrouped_df = groupby_person_date_combo.agg({'TotalSteps':'mean', 'TotalDistance':'mean','TrackerDistance':'mean','LoggedActivitiesDistance':'mean','VeryActiveDistance':'mean','ModeratelyActiveDistance':'mean','LightActiveDistance':'mean','SedentaryActiveDistance':'mean','VeryActiveMinutes':'mean','FairlyActiveMinutes':'mean','LightlyActiveMinutes':'mean','SedentaryMinutes':'mean','Calories':'mean','DayOfWeek':'first'})
print(properlyGrouped_df.iloc[0:9])

#print(df_average_dailySteps_perPersonDate_combo.head())
df_avgMonthlySteps_perPerson = properlyGrouped_df.groupby('Id').agg({'TotalSteps':'mean'})
df_avgMonthlyCalories_perPerson = properlyGrouped_df.groupby('Id').agg({'Calories':'mean'})
df_avgMonthlyDistance_perPerson = properlyGrouped_df.groupby('Id').agg({'TotalDistance':'mean'})
df_avgMonthlyVeryActiveMins_perPerson = properlyGrouped_df.groupby('Id').agg({'VeryActiveMinutes':'mean'})
df_avgMonthlyModerateActiveMins_perPerson = properlyGrouped_df.groupby('Id').agg({'FairlyActiveMinutes':'mean'})
df_avgMonthlyLightlyActiveMins_perPerson = properlyGrouped_df.groupby('Id').agg({'LightlyActiveMinutes':'mean'})
df_avgMonthlySedentaryActiveMins_perPerson = properlyGrouped_df.groupby('Id').agg({'SedentaryMinutes':'mean'})
# add newly generated columns to Dataframe I will use for metric analysis
properlyGrouped_df['AvgMonthlySteps'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlySteps_perPerson['TotalSteps'])
properlyGrouped_df['AvgMonthlyCals'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlyCalories_perPerson['Calories'])
properlyGrouped_df['AvgMonthlyDistance'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlyDistance_perPerson['TotalDistance'])
properlyGrouped_df['AvgVeryActiveMins'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlyVeryActiveMins_perPerson['VeryActiveMinutes'])
properlyGrouped_df['AvgFairlyActiveMins'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlyModerateActiveMins_perPerson['FairlyActiveMinutes'])
properlyGrouped_df['AvgLightlyActiveMins'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlyLightlyActiveMins_perPerson['LightlyActiveMinutes'])
properlyGrouped_df['AvgSedentaryMins'] = properlyGrouped_df.index.get_level_values('Id').map(df_avgMonthlySedentaryActiveMins_perPerson['SedentaryMinutes'])

#check if it appears to be correct. Also check if values change properly at point where it becomes
# next person.
print(properlyGrouped_df.iloc[28:32])
#print(df_avgMonthlySteps_perPerson.head())
# Make copy of properlyGrouped_df for future usage. Don't use original for safety purposes.
properlyGrouped_df_copy = properlyGrouped_df.copy()
print(properlyGrouped_df_copy.columns)

# If adding a ActivityLevel col that categorizes the totalstep for each person at a monthly basis
# by checking where the averages for each person fall, Then you have to make conditions and values.
conditions = [(properlyGrouped_df_copy['AvgMonthlySteps'] < 4000), (properlyGrouped_df_copy['AvgMonthlySteps'] >= 4000) & (properlyGrouped_df_copy['AvgMonthlySteps'] < 8000), (properlyGrouped_df_copy['AvgMonthlySteps'] >= 8000) & (properlyGrouped_df_copy['AvgMonthlySteps'] < 12000), (properlyGrouped_df_copy['AvgMonthlySteps'] >= 12000)]
# make classifications
values = ['Sedentary', 'Lightly', 'Fairly', 'Very']
# generate new col in dataframe
properlyGrouped_df_copy['MonthlyActivityLevel'] = np.select(conditions, values)

# check if activity level col was added prprly.
print(properlyGrouped_df_copy.iloc[27:34])

# Engineer Sleep data
#-------------------------------------------------
# Make new engineered summary stats cols and then merge both frames for metric analysis and vizzes.

# make summary stat cols
df_avgDailyMinsAsleep_overMonth = properlyGroupedSleepDay_df2.groupby('Id').agg({'TotalMinutesAsleep':'mean'})
df_avgTotalTimeInBed_overMonth = properlyGroupedSleepDay_df2.groupby('Id').agg({'TotalTimeInBed':'mean'})
# add newly generated columns to Dataframe I will use for metric analysis
properlyGroupedSleepDay_df2['AvgTotMinsAsleep'] = properlyGroupedSleepDay_df2.index.get_level_values('Id').map(df_avgDailyMinsAsleep_overMonth['TotalMinutesAsleep'])
properlyGroupedSleepDay_df2['AvgTotTimeInBed'] = properlyGroupedSleepDay_df2.index.get_level_values('Id').map(df_avgTotalTimeInBed_overMonth['TotalTimeInBed'])
#print(properlyGroupedSleepDay_df2.iloc[158:163])
print(properlyGroupedSleepDay_df2.index.get_level_values('Id').nunique())
print(properlyGroupedSleepDay_df2.head())
# Multiple issues I'm running into and need to figure out. The orignal dailyActivity already has a small subset of participants, so getting
# reliable sample size is already an issue. Now since I am going to merge sleepday data, which has even fewer participants than
# dailyActivity due to missing monthly recorded info for 9 participannts, with dailyActivity, I'll have even smaller sample size. Add to this
# the issue of missing some daily data rows for certain participants in sleepDay and you have a catastrophe in terms of data that gives reliable insights.
