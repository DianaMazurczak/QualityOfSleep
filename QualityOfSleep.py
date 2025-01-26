import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plottable import Table
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib.gridspec import GridSpec
from sklearn.model_selection import train_test_split
import random

import statsmodels.api as sm
from ISLP.models import (ModelSpec as MS,
 summarize)

data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# C:\Users\diana\PycharmProjects\QualityOfSleep\.venv\Scripts\activate.bat
# pip install ISLP

data[['Systolic', 'Diastolic']] = data['Blood Pressure'].str.split('/', expand=True)
data['Systolic'] = data['Systolic'].astype(int)
data['Diastolic'] = data['Diastolic'].astype(int)
data['BMI Category'] = data['BMI Category'].replace('Normal Weight', 'Normal')
dummies_gender = pd.get_dummies(data['Gender'])
dummies_Occupation = pd.get_dummies(data['Occupation'])
dummies_SpleepDisorder = pd.get_dummies(data['Sleep Disorder'])
numeric_BMICategory = data['BMI Category'].replace(['Normal', 'Overweight', 'Obese'], [0, 1, 2])
data = pd.concat(
    [data[['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Heart Rate',
           'Daily Steps', 'Systolic', 'Diastolic']],
     dummies_gender, dummies_Occupation, dummies_SpleepDisorder, numeric_BMICategory], axis=1)

print(data.columns)
