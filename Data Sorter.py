import os
import pandas as pd

Search_words = ["Water","Study","more","four","five"]
words_totals = len(Search_words)


## This section I am taking the amount of search words there are and creating a list of dataframes and their names 
## Data Frame lists to fill in 
DF_list = []
DF_list2 = [] 
DF_list5 = []
## here I want for every search word ad a new variable 
for words_total in range(0, words_totals):
   dataframes_list = ("df"+ str(words_total))
   DF_list.append(dataframes_list)
   
## here for every word attach the appropriate script to run it 
for i in DF_list:
    dir_loc = ("C:"+ "\\Users\\eliza\\Downloads\\")
    DF_list2.append(dir_loc)

for q in range(0,words_totals):
    paranthesis = ""
    DF_list5.append(paranthesis)


## here I will append the names of the documents found in the download folder 
## I pull the list and append to another list 
grant_list = []
grant_list_updated = []
Grants_combined = []

for i in os.listdir(r'C:\Users\eliza\Downloads'):
   grant_list.append(i)

grants_list = filter(lambda grant: "grant" in grant, grant_list)

new_list = (list(grants_list))
## This is the list of grant documents in the download folder 
grant_list_updated.append(new_list)


## NOW I attach list 2 and 3 by their indexes using a zipper 
DF_list4 = ["".join(pair) for pair in zip(DF_list2,new_list, DF_list5)]
DF_list4

for i in DF_list4:
    DF_list2= (pd.read_csv(i))
    DF_list2.insert(0,"Dummy",1)
     # some code
    Grants_combined.append(DF_list2)

b = pd.concat(Grants_combined, ignore_index=True)
    

Totals = b['Dummy'].sum()

Matrix_DF3 = (b.groupby('OPPORTUNITY TITLE')['Dummy'].sum()/words_totals)*100
print(Matrix_DF3)






    
