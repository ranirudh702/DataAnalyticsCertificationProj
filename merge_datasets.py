# First attempt at merging together both dfs. Check if they display data the way you want/need.
#properlyGroupedSleepDay_df2

left_join_dailyAct_sleepDate_df = pd.merge(properlyGrouped_df_copy, properlyGroupedSleepDay_df2, on=['Id','Date'], how='left')
inner_join_daily_act_sleep_date_df = pd.merge(properlyGrouped_df_copy, properlyGroupedSleepDay_df2, on=['Id','Date'], how='inner')

# edge case: for person 4057192912, not all days in month are recorded for daily activity.
# This person only has 3 days of daily activity recorded, and in the sleep data, he is nonexistent.
# Evaluate efficacy of using a left join by printing this edge case/persn and seeing how
# a left join dataframe actually handles this person.
print(left_join_dailyAct_sleepDate_df.iloc[377:382])
print(left_join_dailyAct_sleepDate_df.columns)
print(left_join_dailyAct_sleepDate_df[left_join_dailyAct_sleepDate_df.index.get_level_values('Id')=='4057192912']['AvgMonthlySteps'])

# As expected, there are a bunch of Nulls that were added in to address this person's absence
# in the sleep data when I joined the two dataframes.


"""


"""