# Analyse the top 50 books on Amazon from 2009 to 2019 
# https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019?resource=download 

# install packages 
import pandas as pd 

df = pd.read_csv("bestsellers.csv")

# data exploration
print(df.head)
print(df.shape)
print(df.columns)
print(df.describe)

# clean data with changes directly made to original df 
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# convert data types 
df["Price"] = df["Price"].astype(float)

# ANALYSIS 
# Author popularity
author_counts = df["Author"].value_counts()
print(author_counts) 

# Average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export results 
author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")