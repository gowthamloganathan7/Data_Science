# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:37:13 2023

@author: Gowtham
"""

import pandas as pd
import numpy as np

df = pd.read_csv("movies_metadata.csv")

########### cleaning the first column ""Adult"" data ###############
print(df.adult.unique()) #check for unique values present in the adult data

print(df.loc[df.adult == "True",:]) #checking which movies are adult movies
print(df.loc[df.adult == "False",:]) #checking which movies are non adult movies

print(df.dtypes)

#it will select not adult movie which as voting of 8 using this find the budget of the movie
x= df.loc[(df.adult == "False") & (df.vote_average >=8 ),"budget"]

print(x)

#this show the data which remaining data which is false and true "~" this symbol NOR
x1 = df.loc[~df.adult.isin(["False","True"]),:]
print(x1)

df = df.loc[df.adult.isin(['False','True']),:] #this stored the data where the adult movie is true or false
print(df.adult.unique())

df.adult = df.adult.map({"True":1,"False":0}) # convert from string to 0/1
print(df)

df.loc[df.adult== 1,:]

######### cleaning the next columns ""belongs to collection"" #################

print(df.belongs_to_collection.unique())

print(df.belongs_to_collection.values[0]) #this will shows the index 0 values present in belongs to collection
'''{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}" '''
#so the data is in string format we need to convert into dictionary and seperate only "name" column

import ast
import numpy as np
ast.literal_eval(df.belongs_to_collection.values[2])['name'] # this convert string to dictionary and show name column from the dictionary

collectionName=[]#list that is used to store a new collection of name
for i in df["belongs_to_collection"].values: #itrating the column
    if i == i: #check if it is a nan
        collectionName.append(ast.literal_eval(i)["name"])#if it is not a nan value it convert string to dictionary and store name column'
    else:
        collectionName.append("Standalone_movie")#it will store the nan values as standalone movie
        continue
df["Collection_name"] = collectionName #it will create a new column in the dataframe and store the new values in it
df=df.drop(columns = ["belongs_to_collection"]) #so we have cleaned the data so there is no need of this column 

##########  cleaning the next columns "" budget column"" ########################

df.budget.values[0] # this is string data type so we need to convert in int
df.budget = df.budget.astype("int64") #casting process converting str to int

df.budget.describe() #summery stats

sum(df.budget == 0)*100/df.shape[0] #checking percentage of null values
# so 80% of datas are having null values
# 1) if budget column is not manditory we can drop this column
# 2) we can interpert the column
# 3) drop all the rows whichs having null values


######### cleaning the next columns "" genres column "" #######################

df.genres.values[0]

import ast
uniquegenre = set([])# created new variable to find unique values in genres
for i in df.genres: # created a loop itrate
    Genres = ast.literal_eval(i) # it will store the converted str to dict into Genres 
    for j in Genres: # it will itrate Genres variable
        uniquegenre.add(j["name"]) #it will sub name column and store it in uninquegenres variable
        
print(uniquegenre)
    
rows= [[]] # create to store a values

genres = list(uniquegenre) # converted set to list and stored it in genres variable

for i in df.genres: #looping genres
    genlist = ast.literal_eval(i) # converting str to list of dict
    moviesgenres = [x["name"] for x in genlist] # name column from the genlist will be looped
    row=[] # created to store a new values 0's and 1's
    for i in genres: # looping genres variable
        row.append(int(i in moviesgenres)) #comparing genres and moviesgenres so if that genres present it will show  1 if not 0
    rows.append(row) #row column will be stores in the rows
    
genre = pd.DataFrame(rows[1:],columns = genres) #it is converting into dataframe rows values will be filled in rows and genres will be make it as columns

df = pd.concat([df,genre], axis = 1) # merging two dataframes axis = 1 mean it will add it as columns axis = 0 will add it in rows

df= df.drop(columns = ["genres"]) # so dropping the genres column

########    cleaning the next column "" homepage""    #########################

df.homepage.values[0]

print(df.homepage.isnull()) # check for null values

df.homepage.isnull().sum()*100/df.shape[0] #check for percentage

df["homepage_present"] = (~df.homepage.isnull()) # created a derived column 

df.homepage_present = df.homepage_present.map({True:1,False:0})  #converted into 0=false and 1=true
print(df.homepage_present)

df= df.drop(columns= ["homepage"]) #so we have derived a new column so we can removed this one


####################  cleaning  """" id column  """"""  #######################

(df.shape[0]-len(df.id.unique())) #it is used to find the number of duplicate present id column

df = df.drop_duplicates(subset = 'id') #dropped duplicate values

(df.shape[0]-len(df.id.unique()))
df.shape

sum(df.id.isnull()) #check for null values

df= df.dropna(subset= "id") #droped the null values

df.id= df.id.astype("int64") #converted string to int

df.id.values[0] 

################  cleaning """imdb id column""""  ############################

df.imdb_id.values[0]

(df.shape[0]-len(df.imdb_id.unique())) #check for duplicate values
df= df.drop_duplicates(subset='imdb_id') #dropping duplicates
(df.shape[0]-len(df.imdb_id.unique()))

################ cleaning  """original_language """"" ########################

df.original_language.values[0] 
len(df.original_language.unique()) #num of unique language
df.original_language.value_counts() #it will shows each language as how many movies
df.original_language.isnull().sum() #it will shows null values
df= df.dropna(subset= ["original_language"]) #dropping the null values

############### cleaning """"original_title""""""" #########################

'''  there two types of titles was therer so need to remove one '''

df.original_title.values[0]
(sum(df.original_title.isnull()),df.shape[0]-len(df.original_title.unique()),(len(df.original_title.unique())*100/df.shape[0])) #original_title
# out: (0, 2060, 95.4631546491653)
(sum(df.title.isnull()),df.shape[0]-len(df.title.unique()),(len(df.title.unique())*100/df.shape[0])) #title

''' so we compared that "title" as more num of duplicate values'''

df= df.drop(columns =["title"]) #deleted the column 
df.columns

df.original_title = df["original_title"].str.lower()
df.original_title = df["original_title"].str.strip()

(sum(df.original_title.isnull()),df.shape[0]-len(df.original_title.unique()),(len(df.original_title.unique())*100/df.shape[0]))
# out: (0, 2103, 95.36845350834692)

################ cleaning "" 'overview' """"  ###########################

df.overview.values[0]
df.overview = df.overview.str.lower()
df.overview = df.overview.str.strip()
df.overview.isnull().sum()
df.loc[df.overview.isnull(),"overview"] = "No overview"  #changing null values into no overview

df.overview.isnull().sum()

################# cleanin """'popularity'"""""   #########################

df.popularity.values[0]
df.popularity = df.popularity.astype("float64")
print(df.popularity.describe())

#z-score
df["z-score_popularity"] = (df.popularity-df.popularity.mean())/df.popularity.std()

#IQR
Q3 = df.popularity.quantile(0.75)
Q1 = df.popularity.quantile(0.25)

IQR= Q3 - Q1
UT = Q3 + (1.5*IQR)
LT = Q1 - (1.5*IQR)

#clip
df.popularity = df.popularity.clip(LT,UT) #it will change the outliers values
df.popularity.describe()

df.popularity.isnull().sum()
df = df.dropna(subset = ["popularity"])
df.popularity.isnull().sum()

df.poster_path.values[0]
df.poster_path.isnull().sum()

################# cleaning """""vote_count"""""" ###########################

df.vote_count.values[0]
df.vote_count.isnull().sum()
df.vote_count.describe()

################# cleaning """"""vote_average""""""########################

df.vote_average.values[0]
df.vote_average.isnull().sum()
df.vote_average.describe()

################ cleaning """""poster_path""""""""#######################

df.poster_path.values[0] #there is no need of this data

df = df.drop(columns= ["poster_path"]) #so we removed this column

################ cleaning """""production_companies""""""#####################

df.production_companies.values[0]

import ast
index = 0
prod1=[]

for prod in df.production_companies:
    prodlist = ast.literal_eval(prod)
    if len(prodlist) > index:
        prod1.append(prodlist[index]["name"])
    else:
        prod1.append("No Producer")
        
df["production1"] = prod1

index = 1
prod2 = []

for prod in df.production_companies:
    prodlist2 = ast.literal_eval(prod)
    if len(prodlist2) > index:
        prod2.append(prodlist2[index]["name"])
    else:
        prod2.append("No Producer")
        
df["production2"] = prod2

df["production1"]= df["production1"].str.lower()
df["production2"]= df["production2"].str.lower()
df["production1"]= df["production1"].str.strip()
df["production2"]= df["production2"].str.strip()
    
df = df.drop(columns = ["production_companies"])




