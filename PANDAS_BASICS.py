# PANDAS BASICS

import pandas as pd
# reading csv file
df=pd.read_csv("csv_path",index_col='Column_head')


def reading():


    # reading the first 5 rows
    df.head(10) # we can pass values as arguments too

    # reading the last number of rows
    df.tail(10) # we can pass values as arguments too

    # a method that gives data type for all columns
    df.info()

    # synt to display more columns, can be applied to rows also
    pd.set_option('display.max_columns',10)
    pd.set_option('display.max_rows',10)

    # for creating a pandas dataframe using dictionaries with keys as colums head and valued lists as contents
    frame=pd.DataFrame(dict)

    # for selecting different columns 
    y=df[['Artist', 'length', 'Genre']] # This will seperate out these columns

    # determining the number of unique elements
    df['Artist'].unique() # returns all unique elements

    df.to_csv('name_of_new.csv') # save this new dataframe


def indexing():
    #.iloc [1:m, 1:n] –  is used to select or index rows based on their position from 1 to m rows and 1 to n columns
    ## select 1st and 4thcolumn
    df.iloc[:,[0,3]]
    ## Select 2nd row and 3rd column value
    df.iloc[[1,2]]

    #loc [[Row_names],[ column_names]] –  is used to select or index rows or columns  based on their name
    ## select value by row label and column label using loc
    df.loc[[1,2,3,4,5],['Name','Score']]

    #ix – indexing can be done by both position and name using ix.
    ## Get all values of column ‘Score’

    df.ix[:,'Score'] 

def value_counts():
    df['Artist'].value_counts(normalise=True)# normalise argument for percentage representation
    # return count of entries , if all unique all are returned  


def row_heading():
    df.set_index('Artist', inplace=True)
    # this will set artist column inplace for row heading and Artists will be row heads

    df.reset_index(inplace=True)
    # if we want to reset the index

    df.sort_index(ascending=True)
    # sort the index(Artist Names) in ascending order

def filtering_data():
    # getting used to equality operators
    df['length']>=6.7 # This will return row wise boolean expressions

    df1=df[df['length']>=6.7] # This will return dataframe for set condition

    filtr= (df['Artist']== "Rahul Johri")
    df[filtr] # will print a dataframe with artist names as Rahul Johri
    # OR
    df.loc[filtr,'Score'] # for condition filtr just scores are given  v 
    df.loc[-filtr,'Score'] # will return all scores whose conditon does not match

    # We can pass conditons too in df.loc

    filt2=(df['length']>=6.7) & (df['Artist']=='Rahul Johri')
    # we use & for and operation and | for or operation 

    filtr3=df['listed_in'].str.contains('Crime TV Shows', na=False)
    df.loc[filtr3,'listed_in']
    # use na =False to skip NaN values 

def data_modification():
    # if changing all columns use assignment
    df.columns=['Nanga','Mai','hoon'] # only for same list length as number of columns

    df.columns= [x.upper() for x in df.columns]  # for converting column heads to all caps

    df.columns= df.columns.str.replace(' ', '_') # for removing spaces

    df.rename(columns={'Artist': 'ter_mummi', 'last_name':'Noi'}, inplace=True) # for changing not all columns
    
    df.loc[2,['Artist','Score']]= ['Mauri Povich','Yes']
    #OR
    df.at[2,'Artist']='Nora Fatehi'

    # Method 1, for data ,manupilation     
    # for series
    df['Artist'].apply(len) # returns length of string in series Artist

    def update_email(email):
        return email.upper()
        
    df['Artist'].apply(update_email) # here we aren't executing the function, we are passing it
    #df.apply() returns function on all the series only,, either rows or columns

    #Method 2 
    # for every object in dataframe
    df.applymap(len) # returns length of string of all objects

    # Method 3
    # for series only, for substitution 
    df['first'].map({"Corey": "Chris", 'Jane':'Joe'}) # replace above mentioned entries and rest replace by NaN

    #Method 4
    # replace, for series only, substitution
    df['first'].replace({"Yes": 0, 'No':1}) # just no NaN replacement

def Add_Remove_Columns_Rows():
    df['Lul']=df['Artist']+df['first'] # creates a new columns concatenating these two strings

    df.drop(columns=['Artist','lenght'], inplace=True) # return a dataframe with these two columns missing 

    df[['first_name','last_name']]=df['Artist'].str.split(' ',expand=True) # will split up on spaces into two columns and assign them

    df.append({'first': 'Tony'}, ignore_index=True)

    # This will add a new row to our dataframe but only add first name, rest all columns NaN
    dat={
        'first':['Tony','Steve']
        'Last':["Stark",'Rogers']
    }
    df2=pd.DataFrame(dat)

    df.append(df2, ignore_index=True)
    filt=df['length']>=6.7
    df.drop(index=df[filt].index) # for removing specific rows 

def sorting_data():

    # FOR SORTING WHOLE DATAFRAME
    df.sort_values(by=['Artist','Length'],ascending=[False,True], inplace=True)
    # will sort the dataframe according to these columns in order of list index,, first by Artist then by length.. First in descending order then ascending
    df.sort_index()
    # by index

    # FOR SORTING A SERIES 
    df['Artist'].sort_values() # will return sorted series

    df['length'].nlargest(10) # will grab the 10 largest values in the series length

    df.nlargest(10,'Length')  # will get the dataframe for 10 largest values of Length  

    df['length'].nsmallest(10) #  will grab the 10 smallest values in the series length

def Grouping_Agrregating_Data():
    df['length'].median() # returns median 

    df.describe()

    # mean- mean of series
    # std- standard deviation
    # 50%- median

    country_grp = df.groupby(['Country'])

    country_grp.get_group('India') # will return dataframe with country only India

    country_grp['Social Media'].value_counts() # will return a dual index result for Social Media counts of different
     
    country_grp['Social Media'].value_counts().loc['India']  # for India

    country_grp['Salary'].median() # will return median salary for all countries

    # Aggregate fucntions

    country_grp['Social Media'].agg(['median','mean']).loc['Canada']  # will return mean and median for Canada

    country_grp['Listed_In'].apply(lambda x:x.str.contains('Crime TV Shows',na=True).sum()).loc['India']
    # returns number of users in India which are Crime TV shows

    Crime_shows=country_grp['Listed_In'].apply(lambda x:x.str.contains('Crime TV Shows',na=True).sum())

    total_respondents=df['Country'].value_counts()
    total_respondents

    # return a dataframe with country and numebr of respondants

    crime_df=pd.concat([Crime_shows,total_respondents], axis='columns')

    # joining two series

    crime_df.rename(columns={'Listed_In':'No.of_crime_shows','Country':'Total_Respondents'},inplace=True)

    # renaming the columns

    crime_df['Percent_Crime_Shows']=(crime_df['No.of_crime_shows']/crime_df['Total_Respondents'])*100

    # creating percentage columns

def cleaning_data():
    df.dropna(axis='index',how='all',subset=['Artist','length']) # axis = index for rows, columns for columns.. how= all if all values are missing, any if any value is missing 
    # removes all the null rows from dataframe 

    df.fillna('NAH BRAH') # replace all NaN values with something

    df['Age']=df['Age'].astype(float) # because np.nan i.e null values are of float data type

    # while using pd.read_csv we can pass na_values= list of values to be considred as a NaN values


def date_data():
    df['Date']= pd.to_datetime(df["Date"], format='') # check format on website

    df.loc[0, 'Date'].day_name() # returns day name

    # for applying it in a series
    df['Date'].dt.day_name()

    df['Date'].min()
    # returns the earliest date

    df['Date'].max()
    # returns the last date

    df['Date'].max()- df['Date'].min()
    # return the difference in days, i.e Timedelta

    filt=(df['Date']>=pd.to_datetime('Formatted date'))
    df.loc[filt]
    # we can filter rows with date too

    # After setting date as index
    df['2019':'2021'] # we can slice with any date measure using this

    df['High'].resample('D') # date offsets check on internet

    df['High'].resample('D').max() # return max values for each day

    df.resample('W').agg({'Close':'mean','High':'max','Low':'min'})

    # applies different fucntions to different columns and ressamples on weekly basis