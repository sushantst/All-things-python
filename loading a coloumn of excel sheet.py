import pandas as pd
file=pd.read_excel('sampl.xls')
# Rep is one of the column of the data set in our excel file named sampl.xls and jardine is one of a name in that list till which our for loop will run.
column_a=file['Rep']
for um in column_a:
	if um =='Jardine':
		break
	print(um)	

	

    
