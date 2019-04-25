#how many genres are present?
print(len(set(music_df.Genre)))
#10

#what are those 10 genres?
print(set(music_df.Genre))
#"Country", "Alternative", "Easy Listening", "Dance", "R&B", "Rock", "Latin", "Popular", "Hip Hop", "Ballad"

#which year had the most hits in the top 100 songs of the 2000s?
music_df.Year.value_counts()
'''
2009  28
2008  19
2003  12
2007  11
2004  9
2006  8
2005  5
2000  4
2001  3
2002  1
'''

#which artist had the most hit songs in the 2000s?
music_df.Artist.value_counts()
#Black Eyed Peas

#which genre did this (aformentioned) artist play?
set(music_df.Genre[music_df.Artist == "Black Eyed Peas"].value_counts()
#Popular

#what year did that artist have the most top 100 songs?
music_df.Year[music_df.Artist == "Black Eyed Peas"].value_counts()
'''
2009  3
2005  1
2003  1
'''

#show the distribution of the top 3 genres over the years 2000-2009
pd.crosstab(music_df.Year, music_df.Genre[music_df.Genre.isin(["Popular", "Ballad", "Country"])])
'''
Genre Ballad  Country Popular
Year
2000    1        0       1
2001    1        0       1
2002    0        0       1
2003    1        1       8
2004    1        2       5
2005    1        0       2
2006    1        2       5
2007    2        1       8
2008    1        1       14
2009    3        5       20
'''
#this table shows the rise of the popular genre after 2006


