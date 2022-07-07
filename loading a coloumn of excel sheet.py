import pandas as pd
file=pd.read_excel('sampl.xls')
column_a=file['Rep']
for um in column_a:
	if um =='Jardine':
		break
	print(um)	

	

    
