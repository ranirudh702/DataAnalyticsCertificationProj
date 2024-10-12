# Google Data Analytics Project

# Bellabeat Fitbit- User Data Science and Marketing Analytics 
***Motivation:***
Analyze the FitBit Fitness Tracker Data to gain insights into how consumers use Fitbit products and discover trends. Health technology is a growing sector that has exploded in popularity, because it gives the power back to the user by enabling intelligent self-motivated data-driven decision making regarding personal health and is based on valid measurable daily data regarding personal health habits. Smart devices have made this transition to the user-driven paradigm by measuring user data and connecting all the data to an application hub to provide useful information to the users. Bellabeat and it's FitBit style watch is one such company and smart watch that enables the users to track their steps taken, calories burned, total minutes of sleep, active hours of the day and much more. This data motivates the users to stay fit and healthy and enables Bellabeat's success.

## Introduction/Scenario:
This is the Google Data Analytics project to see trends in user data for a company known as Bellabeat and act as a market analyst. As a member of the market analysis team, I should analyze trends in user data for the company's product usage. Then, I should provide appropriate data-driven analytics and insights that inform appropriate marketing strategies to bolster user growth, product usage, product utility, and increased customer acquisition. These insights and marketing strategies will benefit the user base and company in the long-term, increase market share, and set us apart from competition.

## Dataset Overview:
A 338 mb public-domain kaggle dataset which is contained in many comma separated files. The public dataset is provided by Kaggle user Mobius. Here is the link to the dataset: https://www.kaggle.com/datasets/arashnic/fitbit Before analyzing the data, it is important to identify the necessary datasets that facilitate optimal data analytics for my analytics objectives such as recommnding marketing strategies. As such, I filtered out the redundant datasets that were provided. The following are the ones I decided to use for the analysis:
* dailyActivity_merged.csv
* sleepDay_merged.csv

  Data Limitations: The data measures a subset of users over a given month time period. Although this is the case, some users may not have data for all the days of the month. Although this is rare, this was accounted for through forward-filling and other bias-mitigation techniques. Sample size may still need to be increased.

# Keystone Northstar Metrics, Visualizations, Insights, and Marketing strategies:
Before describing each step and their accompanying considerations, let us first demonstrate some concrete **northstar visualizations and resulting insights that drove keystone marketing reccomendations** and resulted in measurable **growth in market share**. If you just want to see the visualizations without the added context of the implied insights and marketing strategies, here is the tableau link: https://public.tableau.com/app/profile/anirudh.reddy6675/viz/FitBaseWatchVisualisation/AverageDailyStepsinweekday
  
*Approach*: Drive Customer Satisfaction to impact market share appreciation, user retention, and customer acquisition. Do this through increasing the efficacy of the ability of Bellabeat's product portfolio to positively impact user health outcomes- The best marketing is an effective product.

**Process**: I will first describe each visualization, display it, explain the insights gained from this visualization, and finally give marketing recommendations to shareholders that enable them to act on the insights.

1. Classifying each user by Activity Level Classification
   
   ![image](https://github.com/user-attachments/assets/e3d91baa-4ae4-422f-889e-8e6494efc7c6)
   
   Analysis Technique: Data segmentation and clustering based on a keystone principle. In this case it is customer/user satisfaction measured through the average monthly Activity Level for each user.
   
   **Insights**
   * Showcases to shareholders, the value of data segmentation of the user population by various metrics that signify the keystone metrics of the analysis. 
   * Which users have a low satisfaction level due to poor health outcomes? Identifying at-risk sub-groups in the user population can inform targeted marketing efforts to maintain user-retention.

   **Shareholder Marketing/Feature Recommendations**
   * Target low activity level users and motivate better health outcomes by offering discount deals for Bellabeat subscriptions or products based on weekly movement goals.
   * Curate personalized daily reminders for low activity users. Granulate more fine-grained movement reminders towards certain times of the day, if users input daily schedule on Bellabeat mobile app.
   * Gameify userbase by creating game-like reward structures such as points/xp for meeting daily movement goals. Incentivize low-activity users by offering more xp for meeting daily goals. Meeting a certain xp threshold will naturally raise the monthly Activity Levls which can unlock further benefits such as discounts, custom workouts, and other perks.


2. How much of population belongs to each segment/classification
   ![image](https://github.com/user-attachments/assets/4ff3413f-46f4-484b-b646-d8df374bc70e)

   How much of population sample size belongs to each classification? This classification is calculated by averaging their daily steps over the month and seeing what the resultant value is. If it is high it will clasify as very or fairly. If low, it will be classified low or sedentary.

   **Insights**
   * How many people have a given monthly activity level?
   * How much of population belongs to undesirable classifications? Understanding distribution will inform resultant marketing campaigns to improve user retention and increase market share.
   * If unwanted activity level statuses apply to the population in a manner that is large enough, it will inform if it is worth investing resources into targeting the at-risk population with proper marketing campaigns.
  
   **Shareholder Marketing/Feature Recommendations**
   * The distribution done on this sample size will inform the shareholders how they should generalize to the total Bellabeat user population and accordingly invest resources into the correct marketing campaign.
   * The threshold for too many low-activity users has been met. Start marketing campaign towards at-risk population sub-group through above features of gameification with a reward structure and curated reminders with further schedule engineering if applicable.
   * Work with revenue/accounting department to create discount deals that will motivate user populations.
   * Curate custom celebrity workouts as rewards for meeting exercise/movement goals.

3. Average daily steps for each day of week PER user (SQL/Python visualization AND Tableau visualization)

![image](https://github.com/user-attachments/assets/5c75526b-fc61-46f3-be8f-6aadf2f4f0bb)
![image](https://github.com/user-attachments/assets/4fe43ef8-9fa4-4c56-bb76-d1457dcb20c5)


   Purpose- To show how average daily activity levels vary for users over each day of week in the month timeframe.
   Will show tableau visualization and sql/python visualization. The tableau viz has the ability to interactively filter for each person if you click on the link.

   **Insights**
   * User activity levels tend to vary depending on what day of the week it is.
   * The reason for the variation is due to user work schedules or other weekly commitments that command their time and detention.
   * Gives user knowledge regarding what days tend to be their worst, in terms of exercise, so that they can plan around it or consciously improve it.
     
   **Shareholder Marketing/Feature Recommendations**
   * Use user-oriented data gleaned from this visualization to engineer movement reminders on weekdays that trend downward in activity level.
   * develop feature that cross-references potential user daily schedule data(from app)to see if lower activity levels on given weekdays are attributable to irl commitments(like work) and accordingly curate high intensity exercises to compensate on the same day or on different days.
   * Curate personalized reminders, monetary bonuses or discounts, and other gameification rewards that motivate user to get ahead of historically observed low impact days and compensate beforehand.

4. Correlation between Avg. Caloric expenditure and Activity Level PER user
   ![image](https://github.com/user-attachments/assets/23482878-4ce5-4e82-aec9-4426622db232)

   Correlation between Activity Level and Caloric expenditure
   ![image](https://github.com/user-attachments/assets/cc7c0539-f2c0-4117-b8bb-33f6b9bf9fd2)

   **Insights**
   * Higher user activity begets higher caloric expenditure.
   * Shows users what exercises on a given day lead to high caloric expenditure/output and how to alter daily movement to incorporate more of these movements.

   **Shareholder Marketing/Feature Recommendations**
   *  Use this as evidence based metric to display and convince users to adopt higher intensities during workouts to increase health outcomes.
   *  feature to make users aware of days when their high-intensity exercise exceeded their low-intensity exercise. This will encourage identification of high-intensity exercises/practices that beget positive calorie expenditure and health outcomes.
   *  Motivates users to practice more of the high impact exercises that beget higher caloric expenditures on average. This leads to increased customer satisfaction, retention, and acquisition.
5. Correlation between Activity Level and Amount of time slept
   ![image](https://github.com/user-attachments/assets/a0c61604-3a79-4cff-a62f-3ccda4228ccc)

   ![image](https://github.com/user-attachments/assets/fde8cc82-bce8-4fd0-99b2-c3e4a3d8349f)
   **Insights**
   * It appears that higher activity levels tend to correlate with lower sleep time and/or quality. This is inconclusive though and need more angles of study.
   * Research shows that sleeping closer to a high intensity workout may yield lower sleep quality due to higher endorphins and adrenaline in the body. Another way the data team should study this data to help yield more positive health outcomes for users is to divide the day into morning,afternoon,evening, and night intervals. Then the data should record the times of when the majority of the activity for the workouts ocurred, and determine how the sleep quality/amount is impacted based on what time of day the individual worked out.
   * 
  **Shareholder Marketing/Feature Recommendations**

   *  Implement a data intake study to measure the times/intervals in which most of the user exercise activity occured for each person and day, and then check against how sleep is impacted.
   *  After implementing this study and analyzing the results, the dev team should implement a marketing feature that recommends what time of day workouts should be placed for users so that customers can achieve the optimal amount of sleep while still maintaining a high level of activity. If sleep is sacrificed no matter what as long as there are high intensity workouts, then the right compromise should be found for intensity.


   




