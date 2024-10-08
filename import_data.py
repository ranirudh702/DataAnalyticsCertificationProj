
export import_data as impData
# Import libs u think are necessary for Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 # step 1: mount the gdrive
from google.colab import drive
drive.mount('/content/drive')
  # get data from location inside drive(probably as a fielpath).
file_path1 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv'
# check if this is actually the correct path I typed.
import os
# List files in the directory
data_dir = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16'
files = os.listdir(data_dir)
print(files)

# Step 2: get all locations as filepaths and save in variables and then convert each to pd dataFrame
file_path2 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyCalories_merged.csv'
file_path3 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyIntensities_merged.csv'
file_path4 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailysteps_merged.csv'
file_path5 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv'
file_path6 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv'
file_path7 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlyIntensities_merged.csv'
file_path8 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv'
file_path9 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv'
file_path10 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteCaloriesWide_merged.csv'
file_path11 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesNarrow_merged.csv'
file_path12 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesWide_merged.csv'
file_path13 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteMETsNarrow_merged.csv'
file_path14 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv'
file_path15 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteStepsNarrow_merged.csv'
file_path16 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/minuteStepsWide_merged.csv'
file_path17 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv'
file_path18 = '/content/drive/My Drive/bellabeatCourseraProjPython/kaggle_Bellabeat_Data_CapstoneProj/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv'

df_dailyActivity = pd.read_csv(file_path1)
df_dailyCalories = pd.read_csv(file_path2)
df_dailyIntensities = pd.read_csv(file_path3)
#df_dailySteps = pd.read_csv(file_path4)
df_heartrate_seconds = pd.read_csv(file_path5)
df_hourlyCals = pd.read_csv(file_path6)
df_hourlyIntensities = pd.read_csv(file_path7)
df_hourlySteps = pd.read_csv(file_path8)
df_minuteCalsNarrow = pd.read_csv(file_path9)
df_minuteCalsWide = pd.read_csv(file_path10)
df_minuteIntensitiesNarrow = pd.read_csv(file_path11)
df_minuteIntensitiesWide = pd.read_csv(file_path12)
df_minuteMETsNarrow = pd.read_csv(file_path13)
df_minuteSleep = pd.read_csv(file_path14)
df_minuteStepsNarrow = pd.read_csv(file_path15)
df_minuteStepsWide = pd.read_csv(file_path16)
df_sleepDay = pd.read_csv(file_path17)
df_weightLogInfo = pd.read_csv(file_path18)


# I realized that if I make changes to my dataframes in my cleaning and analysis process, the changes could maybe be discovered as mistakes
# during the analysis and transformation process. To avoid accumulating to many changes to the original dataframes in my analytic process
# and then discovering one of the changes was an error, I will make copies of the dataframes i'm interested in.
df_dailyActivity_copy = df_dailyActivity.copy()
df_sleepDay_copy = df_sleepDay.copy()
df_hourlyIntensities_copy = df_hourlyIntensities.copy()
df_hourlySteps_copy = df_hourlySteps.copy()