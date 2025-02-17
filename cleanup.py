import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
A) Perform a detailed descriptive analysis of the data set.
Use appropriate statistical measures to describe it.
Include at least one statistical graphic.
The descriptive analysis should be aimed at answering the questions below.

B) Perform appropriate statistical hypotheses tests to answer the two questions:
    - Is the age restriction for movies on Disney+ lower than for movies on Netflix?
         Compare the Average* Age of movies in both platforms
    - Is there a difference in Rotten Tomatoes Score for movies on those two platforms?
        Compare the Average* RT of movies in both platforms
* The word 'Average' is being used liberally to represent any statistical analysis
Give reasons for your choice of test.
"""

# Columns need to be assessed whether to keep, drop, or reformat
#   'Unnamed'       -       Drop, ID makes this column redundant
#   ID              -       Keep, cross-reference if titles are not exclusive per platform
#   Title           -       Drop, ID is sufficient to refer to a title, refer back to the title by searching ID in original df
#   Year            -       Drop, no proposed statistical analysis inherently needs the movie's year
#   Age             -       Keep, see notes below
#   RT              -       Keep, see notes below
#   Netflix         -       Keep, will help to identify availability and separate df into dfN
#   Hulu            -       Drop, will not be included in this study
#   Prime Video     -       Drop, will not be included in this study
#   Disney+         -       Keep, will help to identify availability and separate df into dfD
df = pd.read_csv('./MoviesOnStreamingPlatforms.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop(columns=['Title', 'Year', 'Hulu', 'Prime Video'])

# Convert RT into integers
#   The suffix '/100' is removed, dtype remains as object (string)
#   Column is cast as integer to properly use as numerical values
#   NULL still exist, Int64 retains the (lack of) numerical values
df['Rotten Tomatoes'] = df['Rotten Tomatoes'].str.replace('/100', '')
df['Rotten Tomatoes'] = df['Rotten Tomatoes'].astype('Int64')
#   7/9515 NULL RT scores were replaced with the median of the entire column
#   As percentage of missing values was 0.07%, the impact on creating these values appears to be minimal (compare in report, justify with analyses)
df['Rotten Tomatoes'] = df['Rotten Tomatoes'].fillna(df['Rotten Tomatoes'].median())


# Convert Age ratings into categorical integers
#   Unique ratings are converted into integer categorical labels
##print(df.nunique())
df['Age'] = df['Age'].map({'all': 1, '7+': 2, '13+': 3, '16+': 4, '18+': 5})
df['Age'] = df['Age'].astype('Int64')
#   ----------------> EXPERIMENT WITH WAYS TO FILL NULL VALUES IN AN ATTEMPT TO NOT HAVE TO DISCARD <----------------   #
# Mode Imputation
#   Similar to median imputation used for RT score, this instead used the mode (most common value)
#   This method aims to retain the most common categorical label as it fills the NULL values
#   Risk of this method is filling up ~40% of the dataset with the exact same categorical label, creating a definitive bias
# Mode sets missing values into '5', heavily skewing the data as '18+'
# Median sets missing values into '3', heavily skewing data as '13+'
# Both types of fill introduce a massive bias into the dataset, making any analysis invalid
# For sake of completeness, two options are valid points of comparison:
#   Replace all NULL values as tag '0' to indicate a missing value and continue analysis with this new tag in mind
#   Drop all rows with NULL values and make a reduced analysis of the dataset (up to 60% will be used)
df['Age'] = df['Age'].fillna(0)

# df    ->      main dataframe which loads the full dataset
# dfN   ->      df with only Netflix titles ; '_F' variant holds full set ; '_R' variant holds reduced set (Age Rating NULL values)
# dfD   ->      df with only Disney+ titles ; '_F' variant holds full set ; '_R' variant holds reduced set (Age Rating NULL values)
Netflix = df[(df.Netflix == 0)].index
Disney = df[(df['Disney+'] == 0)].index
dfN_F = df.drop(Netflix)
dfN_F = dfN_F.drop(columns=['Netflix', 'Disney+'])
dfD_F = df.drop(Disney)
dfD_F = dfD_F.drop(columns=['Netflix', 'Disney+'])

Netflix_R = dfN_F[(dfN_F.Age == 0)].index
Disney_R = dfD_F[(dfD_F.Age == 0)].index
dfN_R = dfN_F.drop(Netflix_R)
dfD_R = dfD_F.drop(Disney_R)


dfN_F.to_csv('./NetflixCatalogFull.csv', index=False)
dfN_R.to_csv('./NetflixCatalogReduced.csv', index=False)
dfD_F.to_csv('./DisneyCatalogFull.csv', index=False)
dfD_R.to_csv('./DisneyCatalogReduced.csv', index=False)

df.to_csv('./Movies_Clean.csv', index=False)

a = df['Age'].value_counts().get(0, 0)
x = df['Age'].count()
res = a / x * 100
print(res.round(2))
