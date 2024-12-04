import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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