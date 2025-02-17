import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

dfN_F = pd.read_csv('./NetflixCatalogFull.csv')
dfN_R = pd.read_csv('./NetflixCatalogReduced.csv')
dfD_F = pd.read_csv('./DisneyCatalogFull.csv')
dfD_R = pd.read_csv('./DisneyCatalogReduced.csv')

# Box Plot - Rotten Tomatoes (All)
plt.figure(figsize=(7,7))
plt.boxplot(dfN_F['Rotten Tomatoes'], positions=[1], tick_labels=['Netflix Full'], patch_artist=True, notch=True)
plt.boxplot(dfN_R['Rotten Tomatoes'], positions=[2], tick_labels=['Netflix Reduced'], patch_artist=True, notch=True)
plt.boxplot(dfD_F['Rotten Tomatoes'], positions=[3], tick_labels=['Disney+ Full'], patch_artist=True, notch=True)
plt.boxplot(dfD_R['Rotten Tomatoes'], positions=[4], tick_labels=['Disney+ Reduced'], patch_artist=True, notch=True)
plt.yticks(np.arange(0, 101, step=10))
plt.grid()
plt.title('Distribution of Rotten Tomatoes score by streaming platform')
plt.ylabel('Rotten Tomatoes Score')
plt.savefig('./Images/Boxplot.png')
plt.clf()

# Bar Graph - Age
#   x   :   label [0,5]
#   y   :   count (total occurrences)
plt.figure(figsize=(10,5))
x1, y1 = np.unique(dfN_F['Age'], return_counts=True)
x2, y2 = np.unique(dfD_F['Age'], return_counts=True)
plt.bar(x1 - 0.2, y1, 0.4, color='tomato')
plt.bar(x2 + 0.2, y2, 0.4, color='cornflowerblue')
ageRatings = ['Not Given', 'All Ages', '7+', '13+', '16+', '18+']
plt.title('Distribution of Age Rating by streaming platform')
plt.xticks(x1, ageRatings)
for i in range(len(x1)):
    plt.text(i - 0.325, y1[i], y1[i])
for j in range(len(x2)):
    plt.text(j + 0.075, y2[j], y2[j])
plt.legend(['Netflix', 'Disney+'])
plt.xlabel('Age Rating')
plt.ylabel('Amount of titles')
plt.savefig('./Images/BarPlot.png')
plt.clf()

# Line Plot - RT
plt.figure(figsize=(6,4))
dfN_F['Rotten Tomatoes'].value_counts().sort_index().plot()
dfN_R['Rotten Tomatoes'].value_counts().sort_index().plot()

plt.xticks(np.arange(0, 101, step=10))
plt.grid()
plt.title('Frequency of Rotten Tomatoes scores (Netflix)')
plt.xlabel('Rotten Tomatoes score')
plt.ylabel('Amount of titles')
plt.legend(['Netflix Full', 'Netflix Reduced'])
plt.savefig('./Images/LinePlot1.png')

plt.figure(figsize=(6,4))
dfD_F['Rotten Tomatoes'].value_counts().sort_index().plot()
dfD_R['Rotten Tomatoes'].value_counts().sort_index().plot()
plt.xticks(np.arange(0, 101, step=10))
plt.grid()
plt.title('Frequency of Rotten Tomatoes scores (Disney+)')
plt.xlabel('Rotten Tomatoes score')
plt.ylabel('Amount of titles')
plt.legend(['Disney+ Full', 'Disney+ Reduced'])
plt.savefig('./Images/LinePlot2.png')
