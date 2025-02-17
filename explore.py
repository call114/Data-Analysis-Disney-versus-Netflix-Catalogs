import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ranksums
from scipy.stats import mannwhitneyu

df = pd.read_csv('./Movies_Clean.csv')

dfN_F = pd.read_csv('./NetflixCatalogFull.csv')
dfN_R = pd.read_csv('./NetflixCatalogReduced.csv')

dfD_F = pd.read_csv('./DisneyCatalogFull.csv')
dfD_R = pd.read_csv('./DisneyCatalogReduced.csv')

# print first 5 rows
##print(df.head())

# print Column Name, Non-Null Count, and Data Type for each column
##df.info()
##dfN_F.info()
##dfN_R.info()
##dfD_F.info()
##dfD_R.info()

# Count how many rows for each column have a NULL value
#   Age (Rating) has 4177
#   Rotten Tomatoes has 7
#   No other column has NULL values
##print(df.isnull().sum())

# Print percentage of NULL values for each column
##print(round((df.isnull().sum()/df.shape[0])*100, 2))
'''
# Describe most common statistical analysis for the numerical columns
# Numerical Columns:
#   ID              -       int ; 1-index identifier for movie titles
#   Age             -       int ; Age rating of the movie; categorized by integer values to facilitate ease of access
#   Rotten Tomatoes -       int ; Audience rating of the movie
#   Netflix         -       int ; boolean representative of availability
#   Disney+         -       int ; boolean representative of availability
# Statistical Variables (rounded to 2 decimal places):
#   count           -       Amount of rows accounted for
#   mean            -       Arithmetic Mean
#   std             -       Standard Deviation
#   min/max         -       Minimum/Maximum value
#   25/50/75%       -       value at the 25/50/75% position
print(df.describe().round(4))
print(dfN_F.describe().round(4))
print(dfN_R.describe().round(4))
print(dfD_F.describe().round(4))
print(dfD_R.describe().round(4))

a = dfN_R['Age'].count()
b = dfD_R['Age'].count()
print(a)
print(b)
'''
print('F ; N = D:\t', mannwhitneyu(dfN_F['Rotten Tomatoes'], dfD_F['Rotten Tomatoes'], alternative='two-sided').pvalue)
print('F ; N > D:\t', mannwhitneyu(dfN_F['Rotten Tomatoes'], dfD_F['Rotten Tomatoes'], alternative='greater').pvalue)

print('R ; N = D:\t', mannwhitneyu(dfN_R['Rotten Tomatoes'], dfD_R['Rotten Tomatoes'], alternative='two-sided').pvalue)
print('R ; N > D:\t', mannwhitneyu(dfN_R['Rotten Tomatoes'], dfD_R['Rotten Tomatoes'], alternative='greater').pvalue)

##print('N Full:\t\t', dfN_F['Rotten Tomatoes'].median())
##print('N Reduced:\t', dfN_R['Rotten Tomatoes'].median())
##print('D Full:\t\t', dfD_F['Rotten Tomatoes'].median())
##print('D Reduced:\t', dfD_R['Rotten Tomatoes'].median())
